from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def main():
    my_url = "https://google.com"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(my_url)
    driver.quit()


if __name__ == '__main__':
    main()
