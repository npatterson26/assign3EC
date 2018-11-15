import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

FILENAME = "assign2.csv"

def main():
        # Add calculation to list
        stuff = read_list()

        driver = webdriver.Chrome()
        user = "instructor"
        pwd = "instructor1a"
        driver.get("http://n8patty.pythonanywhere.com/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        driver.get("http://n8patty.pythonanywhere.com/product/create/")
        for i in stuff:
            if i[0] == "name":
                continue
            driver.get("http://n8patty.pythonanywhere.com/product/create/")
            driver.find_element_by_xpath("//*[@id=\"id_cust_name\"]/option[2]").click()
            elem = driver.find_element_by_id("id_product")
            name = i[0]
            elem.send_keys(str(name))

            elem = driver.find_element_by_id("id_p_description")
            description = i[1]
            elem.send_keys(str(description))

            elem = driver.find_element_by_id("id_quantity")
            quantity = i[2]
            elem.send_keys(str(quantity))

            elem = driver.find_element_by_id("id_charge")
            charge = i[3]
            elem.send_keys(str(charge))

            time.sleep(3)
            driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        driver.close()


def read_list():
    stuff = []
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            stuff.append(row)
    return stuff


main()
