from _datetime import date, datetime
import unittest
import datetime
import time
import os

from selenium import webdriver
from selenium.webdriver.support.select import Select


class TestBase(unittest.TestCase):
    
    def setUp(self,driver):
        self.driver=driver
       
        
        
    @staticmethod 
    def start_browser(browsername,baseURL="E:\HTML_Pages\Registration.html"):
        print("browser name is:"+browsername)
      
        if browsername=='chrome':
            driver=webdriver.Chrome()
        elif browsername=='firefox':
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Ie()  
            
        driver.get(baseURL)
        driver.set_page_load_timeout(60)
        driver.maximize_window()
        print("Test Start at:"+str(datetime.datetime.now()))
        print("---------------------------------------------")
        return driver
    
    def find_element(self,*loc):  
        return self.driver.find_element(*loc)  
    
    def select_element_from_dropdown(self,*locator):  
        return Select(self.driver.find_element(*locator))            
        
    @staticmethod
    def get_date_time():
       
        dt_format = '%Y%m%d_%H%M%S'
        return datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)
 
    @staticmethod
    def save_screenshot_picture(driver):
     
        date_time = TestBase.get_date_time()
        current_location = "C:/Users/vostro/workspace/WebAutomation"
        screenshot_folder = current_location + '/screenshot/'
        if not os.path.exists(screenshot_folder):
            os.mkdir(screenshot_folder)
 
        picture = screenshot_folder + ' ' + date_time + '.png'
        driver.save_screenshot(picture)
        
        
    def tearDown(self):
        print("---------------------------------------------")
        print("Test environment destroyed.....")
        print("Test END at:"+str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()
        
          
            