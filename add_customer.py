import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        #driver.maximize_window()
        driver.get("http://n8patty.pythonanywhere.com/home/")
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://n8patty.pythonanywhere.com/home/")
        assert "Logged In"
        # Nav Bar
        driver.get("http://n8patty.pythonanywhere.com/home/")
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[1]/a").click()
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[3]/a").click()
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[4]/a").click()

        # Home Nav
        driver.get("http://n8patty.pythonanywhere.com/home/")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div/div/div/div/div/div[1]/div/div/p[2]/a").click()
        driver.get("http://n8patty.pythonanywhere.com/home/")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        driver.get("http://n8patty.pythonanywhere.com/home/")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a").click()
        time.sleep(5)
        # Summary
        driver.get("http://n8patty.pythonanywhere.com/customer_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a").click()
        # Customer Edit
        driver.get("http://n8patty.pythonanywhere.com/customer_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a").click()
        elem = driver.find_element_by_id("id_cust_name")
        elem.clear()
        elem.send_keys("AESOP")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        # Customer Delete
        driver.get("http://n8patty.pythonanywhere.com/customer_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[13]/a").click()
        driver.switch_to.alert.accept()
        #time.sleep(4)
        # Service Add
        driver.get("http://n8patty.pythonanywhere.com/service_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span").click()
        driver.find_element_by_xpath("//*[@id=\"id_cust_name\"]/option[2]").click()
        elem = driver.find_element_by_id("id_service_category")
        elem.clear()
        elem.send_keys("children")
        elem = driver.find_element_by_id("id_description")
        elem.clear()
        elem.send_keys("more children")
        elem = driver.find_element_by_id("id_location")
        elem.clear()
        elem.send_keys("hastings")
        elem = driver.find_element_by_id("id_service_charge")
        elem.clear()
        elem.send_keys("1")

        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        time.sleep(1)
        # Service Edit
        driver.get("http://n8patty.pythonanywhere.com/service_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a").click()
        elem = driver.find_element_by_id("id_service_charge")
        elem.clear()
        elem.send_keys("69")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        # Service Delete
        driver.get("http://n8patty.pythonanywhere.com/service_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[9]/a").click()
        driver.switch_to.alert.accept()
        # Product Add
        driver.get("http://n8patty.pythonanywhere.com/product_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span").click()
        driver.find_element_by_xpath("//*[@id=\"id_cust_name\"]/option[2]").click()
        elem = driver.find_element_by_id("id_product")
        elem.clear()
        elem.send_keys("Takis")
        elem = driver.find_element_by_id("id_p_description")
        elem.clear()
        elem.send_keys("Takis food")
        elem = driver.find_element_by_id("id_quantity")
        elem.clear()
        elem.send_keys("69")
        elem = driver.find_element_by_id("id_charge")
        elem.clear()
        elem.send_keys("69")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        # Product Edit
        driver.get("http://n8patty.pythonanywhere.com/product_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[7]/a").click()
        elem = driver.find_element_by_id("id_charge")
        elem.clear()
        elem.send_keys("69")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        # Product Delete
        driver.get("http://n8patty.pythonanywhere.com/product_list")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a").click()
        driver.switch_to.alert.accept()
        # Change Password
        driver.get("http://n8patty.pythonanywhere.com/home")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/a").click()
        elem = driver.find_element_by_id("id_old_password")
        elem.clear()
        elem.send_keys("instructor1a")
        elem = driver.find_element_by_id("id_new_password1")
        elem.clear()
        elem.send_keys("instructor1a")
        elem = driver.find_element_by_id("id_new_password2")
        elem.clear()
        elem.send_keys("instructor1a")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/p[5]/input").click()
        # Forgot Password / Logout
        driver.get("http://n8patty.pythonanywhere.com/home")
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/ul/li/a").click()
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/p/a").click()
        elem = driver.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("Ovid@ovid.ovid")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/p[2]/input").click()
        # Login again
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        # driver.maximize_window()
        driver.get("http://n8patty.pythonanywhere.com/home/")
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://n8patty.pythonanywhere.com/home/")
        # Register
        driver.get("http://n8patty.pythonanywhere.com/home")
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/ul/li/a").click()
        driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.clear()
        elem.send_keys("Ovid")
        elem = driver.find_element_by_id("first_name")
        elem.clear()
        elem.send_keys("Ovid")
        elem = driver.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("Ovid@ovid.ovid")
        elem = driver.find_element_by_id("id_password")
        elem.clear()
        elem.send_keys("OvidTheDog0")
        elem = driver.find_element_by_id("id_password2")
        elem.clear()
        elem.send_keys("OvidTheDog0")
        driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/p[6]/input").click()


        """""
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This is a test post of text with selenium")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)
        assert "Posted Blog Entry"
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")
        """
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
