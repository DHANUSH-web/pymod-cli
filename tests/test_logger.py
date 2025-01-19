from modules.logger import Logger
import unittest
import datetime


class TestLogger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize logger
        cls.start_time: datetime = datetime.datetime.now()
        cls.stop_time: datetime or None = None
        cls.logger: Logger = Logger(debug=True)

    # setup will be called before every test case
    def setUp(self):
        # TODO: implement this method
        ...

    # Implement logger test cases here

    # tearDown will be called after every test case
    def tearDown(self):
        # TODO: implement this method
        ...

    @classmethod
    def tearDownClass(cls):
        # TODO: implement this method
        ...


if __name__ == '__main__':
    unittest.main()
