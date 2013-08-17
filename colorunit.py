#!/usr/bin/python
#coding: utf-8
"""A nose plugin: Just make the python standard module: nose output with formatted and colorful more like XUnit output.
"""

import os
import sys
import time
import traceback
from nose.plugins import Plugin
from nose.core import TextTestRunner

class MColorStreamForLinux(object):
    def __init__(self, stream):
        try:
            from blessings import Terminal
        except:
            pass
        self.stream = stream
        self.term = Terminal()

    def __getattr__(self, attr):
        if attr in ('stream', '__getstate__'):
            raise AtrributeError(attr)
        return getattr(self.stream, attr)

    def writeln(self, msg=None):
        if msg:
            self.write(msg)
        self.write('\n')

    def red(self, msg):
        self.write(self.term.red + self.term.bold + msg + self.term.normal)

    def green(self, msg):
        self.write(self.term.green + self.term.bold + msg + self.term.normal)

    def yellow(self, msg):
        self.write(self.term.yellow + self.term.bold + msg + self.term.normal)

    def cyan(self, msg):
        self.write(self.term.cyan + self.term.bold + msg + self.term.normal)

    def white(self, msg):
        self.write(self.term.white + self.term.bold + msg + self.term.normal)

    def blue(self, msg):
        self.write(self.term.blue + self.term.bold + msg + self.term.normal)


class MColorStreamForWindows(object):
    pass


class MColorStreamDecorator(object):
    """It's my color stream decorator."""
    def __init__(self, stream):
        if os.name == "nt": # windows
            self.stream = MColorStreamForWindows(stream)
        elif os.name == "posix": # Linux
            self.stream = MColorStreamForLinux(stream)
    
    def __getattr__(self, attr):
        if attr in ('stream', '__getstate__'):
            raise AtrributeError(attr)
        return getattr(self.stream, attr)


class MTextTestRunner(TextTestRunner):

    def __init__(self, stream):
        super(MTextTestRunner, self).__init__()

    def run(self, test):
        result = self._makeResult()
        startTime = time.time()
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
        try:
            test(result)
        finally:
            stopTestRun = getattr(result, 'stopTestRun', None)
            if stopTestRun is not None:
                stopTestRun()
        stopTime = time.time()
        timeTaken = stopTime - startTime
        #result.printErrors()
        if hasattr(result, 'separator2'):
            self.stream.writeln(result.separator2)
        run = result.testsRun
        self.stream.writeln("Ran %d test%s in %.3fs" %
                            (run, run != 1 and "s" or "", timeTaken))
        self.stream.writeln()

        expectedFails = unexpectedSuccesses = skipped = 0
        try:
            results = map(len, (result.expectedFailures,
                                result.unexpectedSuccesses,
                                result.skipped))
        except AttributeError:
            pass
        else:
            expectedFails, unexpectedSuccesses, skipped = results

        infos = []
        if not result.wasSuccessful():
            self.stream.write("FAILED")
            failed, errored = map(len, (result.failures, result.errors))
            if failed:
                infos.append("failures=%d" % failed)
            if errored:
                infos.append("errors=%d" % errored)
        else:
            self.stream.write("OK")
        if skipped:
            infos.append("skipped=%d" % skipped)
        if expectedFails:
            infos.append("expected failures=%d" % expectedFails)
        if unexpectedSuccesses:
            infos.append("unexpected successes=%d" % unexpectedSuccesses)
        if infos:
            self.stream.writeln(" (%s)" % (", ".join(infos),))
        else:
            self.stream.write("\n")
        return result


class ColorUnit(Plugin):
    """print the output with formated and colorful, just more like xunit."""
    name = "colorunit"
    score = 20
    encoding = "UTF-8"

    def __init__(self):
        super(ColorUnit, self).__init__() # involved the Plugin init
        self.stream = MColorStreamDecorator(sys.stderr)
        self.separator1 = "=" * 70
        self.separator2 = "-" * 70
        self.STDOUT_LINE = '\nStdout:\n%s'
        self.STDERR_LINE = '\nStderr:\n%s'
        self.showAll = False
        self.buffer = False
        self.dots = True
        self.descriptions = True
    
    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return "\n".join((str(test)), doc_first_line)
        else:
            return str(test)

    def startTest(self, test):
        self.stream.writeln(self.separator1)
        self.stream.cyan("[RUN\t]")
        self.stream.writeln(self.getDescription(test))
        if self.showAll:
            self.stream.writeln(self.getDescription(test))
            self.stream.writeln(" ... ")
            self.stream.flush()


    def stopTest(self, test):
        self.stream.writeln()
    
    def addSuccess(self, test):
        if self.showAll:
            self.stream.writeln("ok")
        elif self.dots:
            self.stream.green('[OK\t]')
            self.stream.writeln(self.getDescription(test))
            self.stream.flush()

    def addError(self, test, err):
        if self.showAll:
            self.stream.writeln("ERROR")
        elif self.dots:
            self.stream.yellow('[ERROR\t]')
            self.stream.writeln(self.getDescription(test))
            self.stream.writeln(self._exc_info_to_string(err, test))
            self.stream.flush()

    def addFailure(self, test, err):
        if self.showAll:
            self.stream.writeln("FAIL")
        elif self.dots:
            self.stream.red('[FAIL\t]')
            self.stream.writeln(self.getDescription(test))
            self.stream.writeln(self._exc_info_to_string(err, test))
            self.stream.flush()

    def addSkip(self, test, reason):
        if self.showAll:
            self.stream.writeln("SKIP")
        elif self.dots:
            self.stream.blue("[SKIP\t]")
            self.stream.writeln(self.getDescription(test))
            self.stream.writeln("{0}".format(reason))
            self.stream.flush()

    def printErrors(self):
        pass

    def printErrorList(self, flavour, errors):
        pass


    def finalize(self, result):
        #self.stream.writeln(str(result))
        pass
    
    def prepareTestRunner(self, runner):
        self.runner = MTextTestRunner(self.stream)
        return self.runner

    #def formatErr(self, err):
    #    exctype, value, tb = err
    #    return "".join(traceback.format_exception(exctype, value, tb))

    def setOutputStream(self, stream):
        # grab for own use and decorate it.
        return self.stream
        
    def _exc_info_to_string(self, err, test):
        """Converts a sys.exc_info()-style tuple of values into a string."""
        exctype, value, tb = err
        # Skip test runner traceback levels
        while tb and self._is_relevant_tb_level(tb):
            tb = tb.tb_next

        if exctype is test.failureException:
            # Skip assert*() traceback levels
            length = self._count_relevant_tb_levels(tb)
            msgLines = traceback.format_exception(exctype, value, tb, length)
        else:
            msgLines = traceback.format_exception(exctype, value, tb)

        if self.buffer:
            output = sys.stdout.getvalue()
            error = sys.stderr.getvalue()
            if output:
                if not output.endswith('\n'):
                    output += '\n'
                msgLines.append(self.STDOUT_LINE % output)
            if error:
                if not error.endswith('\n'):
                    error += '\n'
                msgLines.append(self.STDERR_LINE % error)
        return ''.join(msgLines)


    def _is_relevant_tb_level(self, tb):
        return '__unittest' in tb.tb_frame.f_globals


    def _count_relevant_tb_levels(self, tb):
        length = 0
        while tb and not self._is_relevant_tb_level(tb):
            length += 1
            tb = tb.tb_next
        return length
