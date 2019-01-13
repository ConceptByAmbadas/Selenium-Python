import unittest
from _datetime import date, datetime
import datetime
import os
import time
import unittest

from PageObject.test_Payment import Payment
from PageObject.test_Registration import Registration
from UtilityFunctions.TestBase import TestBase


class TestRunner(unittest.TestCase):
      
    @classmethod
    def setUpClass(inst):
        print("one")
        inst.driver=TestBase.start_browser("chrome","chrome")
        
    def test_execute_script(self):    
        registration=Registration(self.driver)
        registration.test_do_Registraion("Pravin", "kale", "abc@gmail.com","98787654567", "Pune", "Nagar", "414502", "pravin", "12345", "description")
        payment=Payment(self.driver)
        payment.test_do_payment("Sachin", "12345", "54321", "5000", "Sachin", "12345")
        
    
    @classmethod
    def tearDownClass(inst):
        #print("Test Start at:"+inst.str(datetime.datetime.now()))
        print("---------------------------------------------")
        inst.driver.quit()
     
        

    


if __name__ == "__main__":
    unittest.main()