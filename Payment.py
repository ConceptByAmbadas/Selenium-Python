from lib2to3.pgen2 import driver

from selenium import  webdriver
from selenium.webdriver.support.select import Select


class Payment(object):    
    def __init__(self,driver):
        self.driver=driver
        
        
    def do_payment(self,cust_name,Sorce_acc,Dest_acc,amount,username,password):
        Select(self.driver.find_element_by_xpath("//*[@name='Source_bank']")).select_by_index(2)
        Select(self.driver.find_element_by_xpath("//*[@name='Dest_bank']")).select_by_index(2)
        self.driver.find_element_by_name("Cust_Name").send_keys(cust_name)
        self.driver.find_element_by_name("Sorce_acc").send_keys(Sorce_acc)
        self.driver.find_element_by_name("Dest_acc").send_keys(Dest_acc)
        self.driver.find_element_by_name("amount").send_keys(Dest_acc)
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("alert_button").click()
        
       
       
       
       
       
        
  