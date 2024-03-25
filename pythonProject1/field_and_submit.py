import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def main():
    my_url = "http://homepro.herokuapp.com/quote.php"
    confirm_page = 'http://homepro.herokuapp.com/quoteconfirm.php'
    login = "https://homepro.herokuapp.com/index.php"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(my_url)
    username = driver.find_element(By.NAME, "txtUsername")
    username.send_keys("Raekwon")
    password = driver.find_element(By.NAME, "txtPassword")
    password.send_keys("admin")
    click_login = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/form/input[3]")
    click_login.click()
    if login.startswith(driver.current_url):
        print(f'Test passed {login} {driver.current_url}')
        quote = driver.find_element(By.XPATH, "/html/body/div/div[2]/a[4]")
        quote.click()
    else:
        print(f'Test Failed {login} {driver.current_url}')
        quote = driver.find_element(By.XPATH, "/html/body/div/div[2]/a[4]")
        quote.click()

    name = driver.find_element(By.NAME, "first_name")
    name.send_keys("student")
    email = driver.find_element(By.NAME, "email")
    email.send_keys("student@student.com")
    phone = driver.find_element(By.NAME, "phone")
    phone.send_keys("202-202-2222")
    description = driver.find_element(By.NAME, "comments")
    description.send_keys("Free Quote")
    send_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/form/table/tbody/tr[6]/td/input")
    send_button.click()
    if confirm_page == driver.current_url:
        print(f"Test Passed!{confirm_page} {driver.current_url}")
    else:
        print(f"Test Failed! {confirm_page} {driver.current_url}")
        # website_text =
    success_message = driver.find_element(By.ID, "contact")
    if success_message.text.strip() == "Your request for a free quote has been sent to homepro. You will be contacted within 24 hours. Thank you!":
        print(f"Test Passed!")
    else:
        print("Test Failed!")
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    main()
