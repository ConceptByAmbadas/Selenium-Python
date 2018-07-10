from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from Locators import AllLocators


class Registration(object):
    
    
  
        
    def __init__(self,driver):
        self.driver=driver
        self.first_name=self.driver.find_element_by_name(AllLocators.first_name)
        self.last_name=self.driver.find_element_by_name(AllLocators.last_name)
        self.email=self.driver.find_element_by_name(AllLocators.email)
        self.phone=self.driver.find_element_by_name(AllLocators.phone)
        self.address=self.driver.find_element_by_name(AllLocators.address)
        self.city=self.driver.find_element_by_name(AllLocators.city)
        self.state=self.driver.find_element_by_name(AllLocators.state)
        self.zip=self.driver.find_element_by_xpath(AllLocators.zip)
        self.username=self.driver.find_element_by_xpath(AllLocators.username)
        self.password=self.driver.find_element_by_xpath(AllLocators.password)
        self.hosting=self.driver.find_element_by_xpath(AllLocators.hosting)
        self.comment=self.driver.find_element_by_name(AllLocators.comment)
        self.btn_submit=self.driver.find_element_by_id(AllLocators.btn_submit)
        self.title=self.driver.find_element_by_name(AllLocators.title)
        self.comment=self.driver.find_element_by_name(AllLocators.comment)
        
        

        
    
    #def do_Registraion(self,phone,address,city,zip,username,password,description):
    def do_Registraion(self):
        Select(self.title).select_by_index(2)
        self.first_name.send_keys("Pravin")
        self.last_name.send_keys("Adhav")
        self.phone.send_keys("9878787878")
        self.email.send_keys("pravin@gmail.com")
        self.city.send_keys("pune")
        self.address.send_keys("Khen\d,pune")
        self.zip.send_keys("423425")
        self.username.send_keys("pravin")
        self.password.send_keys("password")
        self.hosting.click()
        Select(self.state).select_by_index(4)
        self.btn_submit.click()
        self.comment.send_keys("No comments")
        self.driver.save_screenshot()
        
        #select(self.driver.find_element_by_xpath("//select[@name='state']"))
        

        
    #self.driver.find_element_by_xpath("//input[@name='first_name']").send_keys(first_Name)
    #self.driver.find_element_by_xpath("//input[@name='first_name']").send_keys(Last_Name)
    