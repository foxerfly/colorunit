import unittest
import colorunit as cu


class Test_ConfReader(unittest.TestCase):
    def setUp(self):
        self.confReader = cu.ConfReader() 
        self.FB_keys = ['error', 'fail', 'keymsg', 'ok', 'run', 'time', 'skip']
        self.Colormap_value = [cu.Fore.YELLOW, cu.Fore.RED, cu.Fore.MAGENTA, 
                cu.Fore.GREEN, cu.Fore.CYAN, cu.Fore.WHITE, cu.Fore.BLUE]

    def test_configSectionMap_When_using_default_colormap(self):
        Fore_return_value = {'error': 'yellow', 'fail': 'red',
                'keymsg': 'magenta','ok': 'green',
                'run': 'cyan','skip': 'blue', 'time': 'white'}
        Back_return_value = {'error': '', 'fail': '', 'keymsg': '',
                'ok': '', 'run': '', 'skip': '', 'time': ''}
        Style_return_value = {'style': 'bright'}
        # test Fore section
        self.confReader.configSectionMap("Fore")
        self.assertEqual(self.confReader.config_map, Fore_return_value)
        # test Back section
        self.confReader.configSectionMap("Back")
        self.assertEqual(self.confReader.config_map, Back_return_value)
        # test Style section
        self.confReader.configSectionMap("Style")
        self.assertEqual(self.confReader.config_map, Style_return_value)

    def test_getValue_When_using_default_colormap(self):
        # test Fore section and Back section
        for index, key in enumerate(self.FB_keys):
           self.assertEqual(self.confReader.getValue("Fore", key),
                   self.Colormap_value[index]) 
           self.assertEqual(self.confReader.getValue("Back", key), "") 
        # test the Style section style value
        self.assertEqual(self.confReader.getValue("Style", 'style'),
                cu.Style.BRIGHT)

    def test_showColorMsg_When_using_default_colormap(self):
        msg = "test messages"
        for index, key in enumerate(self.FB_keys):
            return_value = self.Colormap_value[index] + "" + \
                    cu.Style.BRIGHT + msg + cu.Style.RESET_ALL
            self.assertEqual(self.confReader.showColorMsg(key, msg),
                    return_value)
