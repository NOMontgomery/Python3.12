import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope='module')
def firefox_driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # return the driver for the time being give back value list tuple ect teardown
    yield driver
    driver.quit()
    # return driver
    pass


def test_select_simple_(firefox_driver):
    test_page2 = "https://homepro.herokuapp.com/order.php"
    test_page3 = "http://homepro.herokuapp.com/quote.php"
    my_url = [test_page2, test_page3]
    driver = firefox_driver
    for url in my_url:
        firefox_driver.get(url)
        if driver.current_url == test_page2:
            print(f'{url} match {driver.current_url} testing is running')
            driver.get(url)
            dropdown = Select(driver.find_element(By.NAME, "job_type"))
            dropdown.select_by_index(1)
            assert dropdown.select_by_index(1) == index (1)
            time.sleep(6)
        else:
            print(f'{url} does not match {test_page2} testing is running')
            driver.get(test_page3)
            checkbox = driver.find_element(By.NAME, "subscription")
            checkbox_selected = checkbox.is_selected()
            assert checkbox_selected, "checkbox wasn't selected"
            if checkbox_selected:
                print(f' checkbox is select.')
            else:
                print(f' checkbox is not selected.')
                # time.sleep(6)
        # assert "urls" in firefox_driver.title
        pass


def test_google(firefox_driver):
    firefox_driver.get("https://www.google.com/")
    assert "Google" in firefox_driver.title
    pass


def test_example(firefox_driver):
    firefox_driver.get("https://example.com/")
    assert "Example Domain" in firefox_driver.title
    pass











if __name__ == '__main__':
    pass
    main()