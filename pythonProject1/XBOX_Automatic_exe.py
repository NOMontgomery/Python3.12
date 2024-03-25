import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def buy_game(driver: WebDriver):
    my_url = "https://www.xbox.com/en-US/"
    driver.implicitly_wait(10)
    driver.get(my_url)

    # searching
    search_icon = driver.find_element(By.CSS_SELECTOR, "#search")
    ActionChains(driver) \
        .move_to_element(search_icon).click() \
        .pause(1).send_keys("Devil May Cry 5").send_keys(Keys.ENTER) \
        .pause(1).perform()

    # search page is loaded - click the first result
    first_result_el = driver.find_elements(By.CLASS_NAME, 'f-result-item')[0]
    ActionChains(driver) \
        .move_to_element(first_result_el).click() \
        .pause(1).perform()

    # Click on the drop-down button
    button_el = driver.find_element(
        # either of these two would work:
        # By.CSS_SELECTOR, "div[class^='ButtonWithFlyout-module__buttonContainer'] button")[0]
        By.XPATH, "//div[contains(@class, 'ButtonWithFlyout-module__buttonContainer')]/button")
    ActionChains(driver) \
        .move_to_element(button_el).click() \
        .pause(1).perform()

    # Select first item
    item_el = button_el.find_elements(
        By.XPATH,
        "//div[contains(@class, 'ButtonWithFlyout-module__buttonContainer')]//li")[0]
    ActionChains(driver) \
        .move_to_element(item_el).click() \
        .pause(1).perform()

    button_el = driver.find_element(
        # either should work here too:
        # By.XPATH, "//div[contains(@class, 'AcquisitionButtons-module')]/button")
        By.CSS_SELECTOR, "div[class^='AcquisitionButtons-module'] button")
    ActionChains(driver) \
        .move_to_element(button_el).click() \
        .pause(1).perform()

    print(f"{driver.current_url=}")
