import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def google_search():
    for driver in [webdriver.Firefox(service=Service(GeckoDriverManager().install())),
                   webdriver.Chrome(service=Service(ChromeDriverManager().install()))]:
        gs = 'https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj668_IhoSFAxV55MkDHQVyC-0QPAgJ'
        driver.get(gs)
        driver.implicitly_wait(20)
        actions = ActionChains(driver)
        gs_search = driver.find_element(By.CLASS_NAME, 'gLFyf')
        actions.move_to_element(gs_search).click().send_keys("cats").send_keys(Keys.ENTER).perform()
        actions.pause(5).perform()
        wiki_click = driver.find_element(By.CLASS_NAME, "VuuXrf")
        actions.move_to_element(wiki_click).click().perform()
        wiki_path = '//*[@id="mw-content-text"]/div[1]/p[2]'
        wiki_texts = driver.find_element(By.XPATH, wiki_path)
        confirm_text = 'The cat (Felis catus), commonly referred to as the domestic cat or house cat, is the only domesticated species in the family Felidae. Recent advances in archaeology and genetics have shown that the domestication of the cat occurred in the Near East around 7500 BC. It is commonly kept as a house pet and farm cat, but also ranges freely as a feral cat avoiding human contact. It is valued by humans for companionship and its ability to kill vermin. Because of its retractable claws, it is adapted to killing small prey like mice and rats. It has a strong, flexible body, quick reflexes, sharp teeth, and its night vision and sense of smell are well developed. It is a social species, but a solitary hunter and a crepuscular predator. Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling, and grunting as well as cat body language. It can hear sounds too faint or too high in frequency for human ears, such as those made by small mammals. It also secretes and perceives pheromones.'
        if wiki_texts.text == confirm_text:
            print(f'text does match')
        else:
            print(f'text does not match')
        driver.quit()


if __name__ == '__main__':
    google_search()
