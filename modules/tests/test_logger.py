from logger.logger import Logger
import unittest
import os


class TestLogger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize logger
        ...

    # setup will be called before every test case
    def setUp(self):
        ...

    # Is logger started
    def test_001_is_logger_initialized(self) -> None:
        logger = Logger(file_name=f"{self.test_001_is_logger_initialized.__name__}.log")
        self.assertIsNotNone(logger)
        logger.exit_logger()

    # Is cache folder is created
    def test_002_is_cache_generated(self) -> None:
        Logger(file_name=f"{self.test_002_is_cache_generated.__name__}.log").exit_logger()
        self.assertTrue(os.path.exists("cache"))

    # Did logger successfully created log file in cache folder
    def test_003_is_log_file_generated(self) -> None:
        test_name = self.test_003_is_log_file_generated.__name__
        Logger(file_name=f"{test_name}.log").exit_logger()
        self.assertTrue(os.path.exists(f"cache/{test_name}.log"))

    # Does logger still works even after logger exited.. NO
    def test_004_is_logger_not_accessible_after_exit(self) -> None:
        test_name = self.test_004_is_logger_not_accessible_after_exit.__name__
        logger = Logger(file_name=f"{test_name}.log")
        logger.log(message=test_name)
        logger.exit_logger()

        with self.assertRaises(ValueError) as handler:
            logger.log(message="This log should raise value error")

        self.assertEqual(str(handler.exception), "I/O operation on closed file.")

    # Is logger working after restarting the logger
    def test_005_is_logger_accessible_after_restarting(self) -> None:
        test_name = self.test_005_is_logger_accessible_after_restarting.__name__
        try:
            logger = Logger(file_name=f"{test_name}.log", debug=True)
            logger.log(message=test_name)
            self.assertTrue(os.path.exists(f"cache/{test_name}.log") and logger.is_active())
        except ValueError:
            self.fail("Logger did not restart after reinitializing")
        finally:
            logger.exit_logger()

    # check for total log count
    def test_006_check_for_total_log_count(self) -> None:
        logger = Logger(file_name=self.test_006_check_for_total_log_count.__name__)
        logger.log(message="log1")
        logger.log(message="log2")
        logger.log(message="log3")
        logger.exit_logger()

        self.assertEqual(logger.get_log_count(), 3)

    # Get the total log count of each log levels
    def test_007_logger_each_log_level_count(self) -> None:
        logger = Logger(file_name=f"{self.test_007_logger_each_log_level_count.__name__}.log")
        logger.log(message="error log1", level="error")
        logger.log(message="error log2", level="error")
        logger.log(message="message log1", level="message")
        logger.log(message="debug log1", level="debug")
        logger.log(message="fatal log1", level="fatal")
        logger.log(message="fatal log2", level="fatal")
        logger.log(message="warning log1", level="warning")
        logger.log(message="unknown log1", level="unknown")
        logger.log(message="info log1", level="info")
        logger.log(message="info log2", level="info")
        logger.exit_logger()

        self.assertEqual(logger.get_log_count(), 10)
        self.assertEqual(logger.get_level_count("error"), 2)
        self.assertEqual(logger.get_level_count("warning"), 1)
        self.assertEqual(logger.get_level_count("info"), 2)
        self.assertEqual(logger.get_level_count("debug"), 1)
        self.assertEqual(logger.get_level_count("message"), 1)
        self.assertEqual(logger.get_level_count("fatal"), 2)
        self.assertEqual(logger.get_level_count("unknown"), 1)

    # check if the logger is stopped after calling exit_logger
    def test_008_is_logger_really_stopped(self) -> None:
        logger = Logger(file_name=f"{self.test_008_is_logger_really_stopped.__name__}.log")
        self.assertTrue(logger.is_active())
        logger.exit_logger()
        self.assertFalse(logger.is_active())

    # check for delete log file functionality
    def test_009_is_logger_deleted_log_file(self) -> None:
        test_name = self.test_009_is_logger_deleted_log_file.__name__
        logger = Logger(file_name=f"{test_name}.log")
        self.assertTrue(os.path.exists(f"cache/{test_name}.log"))
        logger.exit_logger()
        logger.delete_log_file()
        self.assertFalse(os.path.exists(f"cache/{test_name}.log"))

    # tearDown will be called after every test case
    def tearDown(self):
        # TODO: implement this method
        ...

    @classmethod
    def tearDownClass(cls):
        ...


if __name__ == '__main__':
    unittest.main()
