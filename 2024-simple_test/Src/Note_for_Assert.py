import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


def main():
    my_url = "https://airbnb.com"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(15)

    driver.get(my_url)
    date_el = driver.find_element(By.XPATH,
                                  '//*[@id="search-tabpanel"]//div[contains(.,"Check in")]//div[contains(.,"Add dates")]')
    date_el.click()

    driver.quit()


if __name__ == '__main__':
    main()
    print('Done!')
# ----------------------------------------------------------------------------------------------------------------------------------

try:
        a = 4 / 0
        print(a)
    except ArithmeticError as e:
        print(f"Division by zero error? {e=}")
        raise
# ------------------------------------------------------------------------------------------------------------------------------------
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# https://peps.python.org/pep-3101/
# https://peps.python.org/pep-0498/
# https://peps.python.org/pep-0701/
n: int = 1222333444
    print(f"{n:,}")

    var: str = 'abc'
    print(f"{var:#>40}")
    print(f"{var:|<40}")
    print(f"{var:_^40}")

    flt: float = 1222333444.123456
    print(f"{flt:,.2f}")

    from datetime import datetime
    now: datetime = datetime.now()
    print(f"{now:%d-%m-%y %H:%M}")
    print(f"{now:%c}")
    print(f"{now:%I%p}")
# -----------------------------------------------------------------------------------------------------------------------
