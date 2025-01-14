import logging
import pytest

def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('/Users/gauravmaan/Desktop/PyTest/FrameWork/Loggings/logfile.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug program")
    logger.info("Information statement")
    logger.warning("warning statement")
    logger.error("error message")
    logger.critical("Do it now")

# class TestLogging:
#     @classmethod
#     def setup_class(cls):
#         logger.info("Setting up class")
#
#     @classmethod
#     def teardown_class(cls):
#         logger.info("Tearing down class")
#
#     def setup_method(self, method):
#         logger.info(f"Setting up method {method.__name__}")
#
#     def teardown_method(self, method):
#         logger.info(f"Tearing down method {method.__name__}")
#
#     def test_example_1(self):
#         logger.info("Running test_example_1")
#         assert 1 == 1
#
#     def test_example_2(self):
#         logger.info("Running test_example_2")
#         assert 2 == 2
#
# if __name__ == "__main__":
#     pytest.main()
