from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture
def setUp():
    global driver,name,address,pincode,email,mobile,password,confpassword
    name = input("Enter Name :")
    address = input("Address :")
    pincode = input("Pincode :")
    email = input("Email :")
    mobile = input("Phone Num :")
    password = input("Password :")
    confpassword = input("Confirm Password :")
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()
    print("Tested Successfully")

def test_validity_userdata(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")
    time.sleep(1)
    driver.find_element_by_name("name").send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(1)
    driver.find_element_by_name("Pincode").send_keys(pincode)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(mobile)
    time.sleep(1)
    driver.find_element_by_name("Email").send_keys(email)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("cnfpass").send_keys(confpassword)
    time.sleep(1)
    driver.find_element_by_name("fcheckbox").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(3)
    driver.close()