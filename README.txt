nose-colorxunit
======================

This is a nose plugin and make the output with formatted and colorful, just more like XUnit.

Installation
-------------

Install with pip::
    
    pip install nose-colorxunit

Uninstall with pip::
        
    pip uninstall nose-colorxunit
    
Install with sourcecode:

    Active your own python virtual environment if you have, Then::

        python setup.py build

        python setup.py install

    If you just want to install it as a super user or using sudo command, please think it again.

Uninstall:

    Just go to your python virtual environment **site-packages** directory, and find **nose_colorxunit-*.*.*-py*.*.egg** , then delete it.

Usage
-----------

First, if you install this in your own python virtual environment, you must active it.

Then, On the terminal::
    
    python test_demo.py --with-colorunit

.. NOTE::
    
    If Working on Ubuntu platform(only test on this platform), you can also use::
        
        python `which nosetests` --with-colorunit

    Without --with-colorunit, the output is just the original.

If you want to see the screenshots on different platform, just view my github repo: https//github.com/walkingnine/colorunit
