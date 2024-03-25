import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def youtube():
    for driver in [webdriver.Firefox(service=Service(GeckoDriverManager().install())),
                   webdriver.Chrome(service=Service(ChromeDriverManager().install()))]:
        yt: str = "https://www.youtube.com/"
        driver.get(yt)
        driver.implicitly_wait(15)
        actions = ActionChains(driver)
        # yt_find_vid = driver.find_element(By.ID, "search-icon-legacy")
        # # yt_find_vid.click()
        # actions.move_to_element(yt_find_vid).click(yt_find_vid)
        actions.pause(1).perform()
        yt_search = driver.find_element(By.XPATH,
                                        "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
        actions.pause(1).perform()
        yt_search.click()
        actions.pause(10).perform()
        yt_search.send_keys("kuro kouch", Keys.ENTER)
        # yt_search.send_keys(Keys.ENTER)
        # actions.move_to_element(yt_search)
        actions.pause(1).perform()
        # actions.click(yt_search).send_keys("kuro kouch").send_keys(Keys.ENTER)
        yt_channel = driver.find_element(By.ID, "main-link")
        yt_channel.click()
        value_title = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-channel-video-player-renderer/div[2]/div/yt-formatted-string"
        yt_title = driver.find_element(By.XPATH, value_title)
        yt_title.click()
        # print(f'{yt_title.get_attribute('innerHTML')}')
        actions.pause(10).perform()
        try:
            skip_button = '.ytp-ad-skip-button-container'
            yt_skip_ad = driver.find_element(By.CSS_SELECTOR, skip_button)
            yt_skip_text = yt_skip_ad.get_attribute('outerHTML')
            yt_skip_text_is = '<span class="ytp-ad-skip-button-container'
            if yt_skip_text.startswith(yt_skip_text_is):
                ActionChains(driver) \
                    .pause(10).perform()
                ActionChains(driver) \
                    .move_to_element(yt_skip_ad).click() \
                    .pause(1).perform()
            else:
                print(f'{yt_skip_text} \n{yt_skip_text_is}')
        except NoSuchElementException:
            pass
        play_button_value = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[35]/div[2]/div[1]/button"
        yt_pause_play_vid = driver.find_element(By.XPATH, play_button_value)
        print(f'this should be the element = {yt_pause_play_vid.get_attribute('outerHTML')}')
        play_pause_text = yt_pause_play_vid.get_attribute('outerHTML')
        play_button_text = '<button class="ytp-play-button ytp-button" aria-keyshortcuts="k" data-title-no-tooltip="Play" aria-label="Play keyboard shortcut k" title="Play (k)"><svg height="100%" version="1.1" viewBox="0 0 36 36" width="100%"><use class="ytp-svg-shadow" xlink:href="#ytp-id-127"></use><path class="ytp-svg-fill" d="M 12,26 18.5,22 18.5,14 12,10 z M 18.5,22 25,18 25,18 18.5,14 z" id="ytp-id-127"></path></svg></button>'
        if play_pause_text == (play_button_text):
            print(f'{play_pause_text} does not = \n{play_button_text}')
        else:
            yt_pause_play_vid.click()
        actions.pause(10).perform()
        try:
            # placeholder = '//*[@id="placeholder-area"]'
            yt_leave_comment = driver.find_element(By.XPATH, '//*[@id="placeholder-area"]')
            # yt_leave_comment.click()
            actions.move_to_element(yt_leave_comment).click().perform()
            print(f'current url {driver.title}')
            driver.back()
            print(f'current url {driver.title}')
            actions.perform()
        except NoSuchElementException:
            pass

        time.sleep(3)
        # driver.quit()


if __name__ == '__main__':
    youtube()
