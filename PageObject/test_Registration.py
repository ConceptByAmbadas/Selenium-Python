from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from UtilityFunctions.Locators import Registration_locators
from UtilityFunctions.TestBase import TestBase


class Registration(TestBase):
    
    
    locator_dictionary={
        "title":(By.NAME,"title"),
        "first_name":(By.NAME,"first_name"),
        "last_name":(By.NAME,"last_name"),
        "email":(By.NAME,"email"),
        "phone":(By.XPATH,"//*[@name='phone']"),
        "address":(By.XPATH,"//*[@name='address']"),
        "city":(By.XPATH,"//*[@name='city']"),
        "state":(By.XPATH,"//*[@name='state']"),
        "zip":(By.NAME,"zip"),
        "username":(By.NAME,"username"),
        "password":(By.NAME,"password"),
        "comment":(By.NAME,"comment"),
        "btn_submit":(By.ID,"btn_submit"),
        "hosting":(By.XPATH,"//input[@name='hosting']")
        
      }
        
    def __init__(self,driver):
        self.driver=driver
        
        
        

        
    
    #def do_Registraion(self,phone,address,city,zip,username,password,description):
    def test_do_Registraion(self,first_name,last_name,email,phone,address,city,zip,username,password,description):
        
        self.select_element_from_dropdown(*self.locator_dictionary['title']).select_by_value("Mr.")
        self.find_element(*self.locator_dictionary['first_name']).send_keys(first_name)
        self.find_element(*self.locator_dictionary['last_name']).send_keys(last_name)
        self.find_element(*self.locator_dictionary['phone']).send_keys(phone)
        self.find_element(*self.locator_dictionary['address']).send_keys(address)
        self.find_element(*self.locator_dictionary['email']).send_keys(email)
        self.find_element(*self.locator_dictionary['city']).send_keys(city)
        self.find_element(*self.locator_dictionary['zip']).send_keys(zip)
        self.find_element(*self.locator_dictionary['username']).send_keys(username)
        self.select_element_from_dropdown(*self.locator_dictionary['state']).select_by_index(2) 
        self.find_element(*self.locator_dictionary['password']).send_keys(password)
        self.find_element(*self.locator_dictionary['comment']).send_keys(description)
        self.find_element(*self.locator_dictionary['hosting']).click()
        self.find_element(*self.locator_dictionary['password']).send_keys(password)
        self.find_element(*self.locator_dictionary['btn_submit']).click()
        TestBase.save_screenshot_picture(self.driver)      
        
        
        """Select(self.title).select_by_index(2)
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
        self.comment.send_keys("No comments")
        self.btn_submit.click()
        TestBase.save_screenshot_picture(self.driver)"""
       
       
        
       
    