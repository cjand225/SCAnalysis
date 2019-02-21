import unittest

import threading
from SCAnalysis.Application.App import App


class testApp(unittest.TestCase):

    def setUp(self):
        pass

    def testInitialization(self):
        MyApp = App()
        self.assertIs(MyApp.__class__, App)

    def testRunning(self):
        MyApp = App()
        myThread = threading.Thread(target=MyApp.run())
        myThread.start()
        MyApp.exit()
        myThread.join()
