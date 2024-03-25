import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
my_url = "https://twitter.com/home?lang=en"
driver.get(my_url)
driver.maximize_window()
print(f"URL: {driver.current_url}\n\tTitle:{driver.title}")
if driver.current_url == my_url:
    print("test succeeded!")
else:
    print("Test Failed!")
time.sleep(5)
driver.quit()
