import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

homepro = "http://homepro.herokuapp.com/quote.php"


def main():
    my_url = "https://homepro.herokuapp.com/quote.php"
    driver2 = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(my_url)
    send_btn = driver.find_element(By.XPATH, "//input[@value='send']")
    send_btn.click()
    alert = driver.switch_to.alert
    driver.switch_to.g
    print(alert.text)
    alert.accept()
    driver.quit()

# if __name__ == '__main__':
#     main()
