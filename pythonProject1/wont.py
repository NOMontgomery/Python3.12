import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

homepro = "http://homepro.herokuapp.com/quote.php"


def main():
    my_url = "https://www.xbox.com/en-US/"
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    for driver in [webdriver.Chrome(service=Service(ChromeDriverManager().install())),
                   webdriver.Firefox(service=Service(GeckoDriverManager().install()))]:
        driver.implicitly_wait(10)
        driver.get(my_url)
        act_que = ActionChains(driver)
        # Should click the search bar icon to un hide the search bar
        search_icon = driver.find_element(By.CSS_SELECTOR, "#search")
        search_icon.click()
        # act_que.move_to_element(search_icon)
        # act_que.pause(1)
        # act_que.double_click(search_icon)
        # Search bar should be visible
        act_que.pause(1)
        # Take you the search page for Devil May Cry 5
        search_bar = driver.find_element(By.CSS_SELECTOR, "#cli_shellHeaderSearchInput")
        search_bar.click()
        # act_que.move_to_element(search_bar)
        # act_que.pause(1)
        # act_que.click(search_bar)
        search_bar.send_keys("Devil May Cry 5")
        search_bar.send_keys(Keys.ENTER)
        act_que.pause(1)
        # act_que.send_keys("Devil May Cry 5")
        # act_que.pause(1)
        # act_que.send_keys(Keys.ENTER)
        act_que.pause(10)
        # Take you the search page for Devil May Cry 5
        dm5 = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[2]/div[1]/div/div[2]/div[1]/h3/a')
        dm5.click()
        # act_que.move_to_element(dm5)
        act_que.pause(1)
        # act_que.click(dm5)
        # # Take you to the page to purchase Devil May Cry 5 page
        # act_que.pause(1)
        # # take you to the page to purchase Devil May Cry 5 page
        dm5_buy = driver.find_element(By.CSS_SELECTOR,
                                      '#PageContent > div > div:nth-child(1) > div.ModuleContainer-module__container___pkhPl.ProductDetailsHeader-module__container___zvKSX > div.FadeContainers-module__fadeIn___5xlsD.FadeContainers-module__widthInherit___5fuOa > div > div > button')
        dm5_buy.click()
        # act_que.move_to_element(dm5_buy)
        # act_que.click(dm5_buy)
        # should click the wishlist link
        act_que.pause(1)
        act_que.perform()
        # If the customer isn't sign in then you should be redirected to sign to finished adding game to "Wishlist"
        login = "https://login.live.com/oauth20_authorize.srf?client_id=1f907974-e22b-4810-a9de-d9647380c97e&scope=xboxlive.signin+openid+profile+offline_access&redirect_uri=https%3a%2f%2fwww.xbox.com%2fauth%2fmsa%3faction%3dloggedIn%26locale_hint%3den-US&response_type=code&state=eyJpZCI6ImEwZTQ2NzJjLTM5ZmEtNGJkMi05NWVkLTU3MjU4MDg3YTJhZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3d%7chttps%253A%252F%252Fwww.xbox.com%252Fen-us%252Fgames%252Fstore%252FDevil-May-Cry-5%252FBNLG5J5KDVJ3&response_mode=fragment&nonce=a58f01c7-2cfb-44f3-ae38-51e870273a35&prompt=select_account&code_challenge=E6e80LKZ6ns54D82vT3hNUtX-9laqW8SCL1kwDGqayg&code_challenge_method=S256&x-client-SKU=msal.js.browser&x-client-Ver=3.7.0&uaid=07122a65ff1b4f2bbd7240eeb67cc6c4&msproxy=1&issuer=mso&tenant=consumers&ui_locales=en-US&client_info=1&epct=PAQABDgEAAADnfolhJpSnRYB1SVj-Hgd8eRev6EgOGOvsxZu66Ei5-6wLxrtbQHIU_nvey4amZofCQW79IAkLKTI8VtX1nitSUnrve3rZzKWbsoXvwKMbguQZrnhiXAn0Wz7PbbS6Q25P1vMi0imLfwYj4Hdm_LPXK6sCy2R8E1th7ioRcdPs4EtPS875fd0Q5cHsMvGL1yxSlmCFhjUEpVFKCl55k1u-sySvoH3reNQUalo5V9aI6CAA&jshs=0#"
        if login == driver.current_url:
            print(f' Is true test concluded')
        else:
            print(f'Is not true test has failed')
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()
