import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


def main():
    # test_page = "http://homepro.herokuapp.com/index"
    test_page2 = "https://homepro.herokuapp.com/order.php"
    test_page3 = "http://homepro.herokuapp.com/quote.php"

    my_url = [test_page2, test_page3]

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    for url in my_url:
        driver.get(url)
        if driver.current_url == test_page2:
            print(f'{url} match {driver.current_url} testing is running')
            driver.get(url)
            dropdown = Select(driver.find_element(By.NAME, "job_type"))
            dropdown.select_by_index(1)
            time.sleep(6)
        else:
            print(f'{url} does not match {test_page2} testing is running')
            driver.get(test_page3)
            checkbox = driver.find_element(By.NAME, "subscription")
            checkbox_selected = checkbox.is_selected()
            if checkbox_selected:
                print(f' checkbox is select.')
            else:
                print(f' checkbox is not selected.')
                time.sleep(6)

    driver.quit()


if __name__ == '__main__':
    main()
