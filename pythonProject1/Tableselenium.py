import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

homepro = "http://homepro.herokuapp.com/quote.php"


def main():
    # my url = "homepro = "http://homepro.herokuapp.com/quote.php""
    driver2 = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # print("This website url is: " + browser.current_url)
    web_site = ("http://the-internet.herokuapp.com/tables",
                "https://the-internet.herokuapp.com/tables")
    # driver.get('http://the-internet.herokuapp.com/tables')
    # driver2.get("http://the-internet.herokuapp.com/tables")
    # table = driver.find_element(By.ID, "table1")
    # rows = table.find_element(By.TAG_NAME, "tr")
    # all_cells = table.find_elements(By.TAG_NAME, "td")
    for url in web_site:
        driver.get("http://the-internet.herokuapp.com/tables")

        if url == driver.current_url:
            print(f'\n\'if block is running\'\n\t{url} == {driver.current_url}')
            driver.get("http://the-internet.herokuapp.com/tables")
            table = driver.find_element(By.ID, "table1")
            rows = table.find_elements(By.TAG_NAME, "tr")
            all_cells = table.find_elements(By.TAG_NAME, "td")
            for row in rows:
                print(row.text)
            for cell in all_cells:
                print(cell.text)
            time.sleep(1)
            driver.quit()
        else:
            print(f"\n Else block is running \n\t{url} does not equals {driver2.current_url}")
            driver2.get("http://the-internet.herokuapp.com/tables")
            table = driver2.find_element(By.ID, "table1")
            rows = table.find_elements(By.TAG_NAME, "tr")
            all_cells = table.find_elements(By.TAG_NAME, "td")
            for row in rows:
                print(row.text)
            for cell in all_cells:
                print(cell.text)
            time.sleep(1)
            driver2.quit()

    # print each row
    # for row in rows:
    #     print(row.text)
    # # print all cells
    # for cell in all_cells:
    #     print(cell.text)

    driver.quit()


if __name__ == '__main__':
    main()
