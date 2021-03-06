
from unittest import TestCase
from unittest import mock
from simplefsapp.simplefsapp import SimpleFSApp


class SimpleFSAppTests(TestCase):
    """
    Test SimpleFSApp.
    """
    def setUp(self):
        self.app = SimpleFSApp()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append('inputdir') # you may want to change this inputdir mock
        args.append('/tmp')  # you may want to change this outputdir mock
        args.append('--dir')
        args.append('./')

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        # write your own assertions
        self.assertEqual(options.outputdir, '/tmp')
