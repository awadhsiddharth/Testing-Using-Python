import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchText(unittest.TestCase):
    def setUp(self):
        self.p_name = input("Enter Product Name : ")
        self.driver = webdriver.Chrome("chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.amazon.in/")

    def test_search_result(self):
        searchBox = self.driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        searchBox.send_keys(self.p_name)

        submitBtn = self.driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
        submitBtn.click()

        elementsCount = self.driver.find_elements(By.XPATH, '//*[@data-component-type="s-search-result"]')
        # print("Elements Count",len(elementsCount))
        self.assertEqual(20, len(elementsCount))
    

if __name__ == '__main__':
    unittest.main()

    