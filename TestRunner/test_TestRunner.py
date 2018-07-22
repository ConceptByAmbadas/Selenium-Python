import unittest
import pytest
import allure
from _datetime import date, datetime

from PageObject.test_Payment import Payment
from PageObject.test_Registration import Registration
from UtilityFunctions.TestBase import TestBase


class TestRunner(unittest.TestCase):
      
    def test_execute(self):
        print("one")
        self.driver=TestBase.start_browser("chrome","chrome")
        registration=Registration(self.driver)
        registration.do_Registraion("Pravin", "kale", "abc@gmail.com","98787654567", "Pune", "Nagar", "414502", "pravin", "12345", "description")
        payment=Payment(self.driver)
        payment.do_payment("Sachin", "12345", "54321", "5000", "Sachin", "12345")
        
    
         
        

    


if __name__ == "__main__":
    unittest.main()