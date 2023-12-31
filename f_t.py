from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element('h1').text
        self.assertIn('To-Do',header_text)
        self.fail("Finish The test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')