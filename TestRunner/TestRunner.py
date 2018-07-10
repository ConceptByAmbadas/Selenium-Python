import unittest

from selenium import webdriver

from Payment import Payment
from Registration import Registration


class Runscript(unittest.TestCase):
    
  
        
        driver=webdriver.Chrome()
        driver.set_page_load_timeout(60)
        driver.maximize_window()
        driver.get("E:\HTML_Pages\Registration.html")
        #driver.refresh()
   
       
         
        
    
        registration=Registration(driver)
        payment=Payment(driver)
       # registration.do_Registraion("Pravin", "Kale", "abc@gmail.com","9876767676","36 china town","Pune","414502","Pravin","IPL1234","Description")
        registration.do_Registraion()
        payment.do_payment("Sachin", "12345", "54321", "5000", "Sachin", "12345")


        if __name__ == '__main__':
            unittest.main()   

