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
    # driver2 = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    for driver in [webdriver.Firefox(service=Service(GeckoDriverManager().install())),
                   webdriver.Chrome(service=Service(ChromeDriverManager().install()))]:
        driver.get(my_url)
        driver.implicitly_wait(10)
        driver.get(my_url)
        form_el = driver.find_element(By.NAME, 'form')
        act_que = ActionChains(driver)
        username_textbox = form_el.find_element(By.NAME, 'txtUsername')
        act_que.move_to_element(username_textbox)
        act_que.pause(1)
        act_que.click(username_textbox)
        act_que.pause(1)
        act_que.send_keys('learnixUser')
        act_que.pause(1)
        pswordtxtbox = form_el.find_element(By.NAME, 'txtPassword')
        act_que.move_to_element(pswordtxtbox)
        act_que.pause(1)
        act_que.click(pswordtxtbox)
        act_que.pause(1)
        act_que.send_keys('SuperSecret')
        act_que.pause(1)
        act_que.click(form_el.find_element(By.NAME, 'Submit'))
        act_que.perform()

        if driver.find_element(By.TAG_NAME, "Hi").text.strip() == "Logged in successfully":
            print(f' Login is succesful.')
        else:
            print(f'login failed')
        time.sleep(3)
        driver.quit()


if __name__ == '__main__':
    main()
