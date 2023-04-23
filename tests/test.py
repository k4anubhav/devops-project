import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class WebserverTest(unittest.TestCase):

    def setUp(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)

    def test_title(self):
        self.driver.get("http://localhost")
        self.assertIn("Hello world", self.driver.find_element(By.TAG_NAME, "body").text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
