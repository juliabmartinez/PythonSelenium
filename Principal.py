from selenium import webdriver
import unittest
import time


class Items(unittest.TestCase):
   def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://www.dafiti.com.ar/?placeholder&gclid=CjwKCAiA35rxBRAWEiwADqB372y7NtNjgw6dgXfHJRTUM_duMa5P9DFfeI9QyiOLGckrvciL4NkX4RoCLpUQAvD_BwE')


    def test_view_item_page(self):
        self.driver.find_element_by_id('searchInput').send_keys('vestidos')
        self.driver.find_element_by_name('submit').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="2:AL560AT48FFVAR"]/div/img').click()
        title = self.driver.find_element_by_xpath("//h2[@itemprop='brand']").text
        self.assertEqual(title, 'Al Aniz')



   def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

