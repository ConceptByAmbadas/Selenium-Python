import unittest

from selenium import webdriver

from PageObject.Payment import Payment
from PageObject.Registration import Registration
from UtilityFunctions.TestBase import TestBase

class Runscript(unittest.TestCase):
        driver=webdriver.Chrome()
        driver=TestBase.start_browser("chrome")
        registration=Registration(driver)
        payment=Payment(driver)
        registration.do_Registraion("Pravin", "kale", "abc@gmail.com","98787654567", "Pune", "Nagar", "414502", "pravin", "12345", "description")
        payment.do_payment("Sachin", "12345", "54321", "5000", "Sachin", "12345")
        

        if __name__ == '__main__':
            unittest.main()  
        

