import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

homepro = "http://homepro.herokuapp.com/quote.php"


def main():
    my_url = "https://homepro.herokuapp.com/quote.php"
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(my_url)
    print(f"This website url is: {driver.current_url}")
    # Check whether the URL of the page opened in the browser matches the URL in page variable.
    # If so, the correct page was opened.
    if driver.current_url.startswith(my_url):  # my_url == driver.current_url:
        print("Test Passed!")
    else:
        print("Test Failed!")
        time.sleep(5)
        driver.quit()
