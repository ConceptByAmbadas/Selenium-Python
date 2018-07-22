
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from UtilityFunctions.TestBase import TestBase


class Payment(TestBase):    
    def __init__(self,driver):
        self.driver=driver
        
    locator_dictionary={
        "source_bank":(By.NAME,"Source_bank"),
        "Dest_bank":(By.NAME,"Dest_bank"),
        "Cust_Name":(By.NAME,"Cust_Name"),
        "Sorce_acc":(By.XPATH,"//*[@name='Sorce_acc']"),
        "Dest_acc":(By.XPATH,"//*[@name='Dest_acc']"),
        "amount":(By.NAME,"amount"),
        "username":(By.NAME,"username"),
        "password":(By.NAME,"password"),
        "alert_button":(By.ID,"alert_button"),
        "popup_ok":(By.ID,"popup_ok")
        
        }    
    def do_payment(self,cust_name,Sorce_acc,Dest_acc,amount,username,password):
       
        self.select_element_from_dropdown(*self.locator_dictionary['source_bank']).select_by_visible_text("HDFC")
        self.select_element_from_dropdown(*self.locator_dictionary['Dest_bank']).select_by_visible_text("SBI")        
        self.find_element(*self.locator_dictionary['Cust_Name']).send_keys(cust_name)
        self.find_element(*self.locator_dictionary['Sorce_acc']).send_keys(Sorce_acc)
        self.find_element(*self.locator_dictionary['Dest_acc']).send_keys(Dest_acc)
        self.find_element(*self.locator_dictionary['amount']).send_keys(amount)
        self.find_element(*self.locator_dictionary['username']).send_keys(username)
        self.find_element(*self.locator_dictionary['password']).send_keys(password)
        self.find_element(*self.locator_dictionary['alert_button']).click()
        self.find_element(*self.locator_dictionary['popup_ok']).click()
        
        
        
        
       
       
       
       
       
        
  