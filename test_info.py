# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def spider(comp_name):
    ret_list = []
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    options = Options()
    options.add_argument('-headless')

    driver = webdriver.Firefox(firefox_profile=profile, options=options)

    driver.get("https://www.zaubacorp.com/")
    driver.set_window_size(890, 751)
    driver.find_element(By.ID, "searchid").send_keys(comp_name)
    driver.find_element(By.ID, "edit-submit--3").click()
    try:
        driver.find_element(By.CSS_SELECTOR, "a > h5").click()
        dir_name = driver.find_element(By.XPATH,
                                       "/html/body/div[6]/div/div[1]/section/div[3]/section/div[2]/div[1]/div[7]/table/tbody/tr[1]/td[2]/p/a").text
        email = driver.find_element(By.CSS_SELECTOR, ".col-lg-6 > p:nth-child(1)").text
        driver.quit()  # exit all browser windows
        email = remove_prefix(email, "Email ID: ")
        ret_list.append(dir_name)
        ret_list.append(email)
        return ret_list
    except:
        a=[n,n]
        return a


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text
