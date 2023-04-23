import unittest

from selenium import webdriver


class WebserverTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get("http://localhost")
        self.assertIn("Hello world", self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
