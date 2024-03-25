import glob
import os
import time
import hashlib
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def hash_it(path):
    with open(path, 'rb') as f:
        hasher = hashlib.md5()
        hasher.update(f.read())
        return hasher.hexdigest()


directory = 'C:/Users/User/PycharmProjects/pythonProject1/compare_image'
remote_img = "{}/{}".format(directory, "remote.png")
local_img = "{}/{}".format(directory, "Imgine1_copy.tif")


def compare_image():
    home_page = 'https://learnix-eshop-test.herokuapp.com/'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(home_page)
    xpath_logo = '/html/body/div[5]/div[2]/div[2]/section/div/div[3]/div/div[1]/div/a[1]/img'
    web_element_pic = driver.find_element(By.XPATH, xpath_logo).get_attribute("src")
    urllib.request.urlretrieve(web_element_pic, remote_img)
    time.sleep(2)
    driver.quit()

    system_logo_hash = hash_it(local_img)
    web_element_img_hash = hash_it(remote_img)
    assert system_logo_hash == web_element_img_hash, "hashes do not match. {} vs {}".format(system_logo_hash,
                                                                                            web_element_img_hash)
    print(f'{system_logo_hash} vs {web_element_img_hash}')


if __name__ == '__main__':
    compare_image()
