import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def main():
    my_url = "https://google.com"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    urls = ['https://twitter.com/home',
            'https://myspace.com/',
            'https://animefreak.video/',
            'https://www.animepro.de/',
            'https://www.gamespot.com/',
            ]
    # driver.quit()

    for url in urls:
        driver.get(url)
        print(f'this website url is {driver.current_url}')
        if url == driver.current_url:

            print(f'Test Passed {url} match {driver.current_url}')
        else:
            print(f'Test fail {url} does not match {driver.current_url}')

        time.sleep(2)

        # driver.quit()


if __name__ == '__main__':
    main()
