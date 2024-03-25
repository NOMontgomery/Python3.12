import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def firefox_driver():
    # setup
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    # teardown
    driver.quit()
    # return driver


def test_google(firefox_driver):
    firefox_driver.get("https://google.com")
    assert "Google" in firefox_driver.title
    pass


def test_example(firefox_driver):
    firefox_driver.get("https://example.com/")
    assert "Example Domain" in firefox_driver.title

def my_range(start, stop, step):
    n = start
    while n < stop:
        yield n
        n += step


@pytest.fixture(scope='function')
def firefox_driver_old(request):
    # setup
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # teardown / cleanup - old style
    def cleanup():
        driver.quit()

    request.addfinalizer(driver.quit)

    # proceed with the test(s)
    return driver

some_list = [0, 7, 'a', 'b']


@pytest.fixture(params=some_list)
def basic_param_data(request):
    return request.param

@pytest.mark.skipif(sys.version_info < (4, 7), reason="requires python3.7 or higher")
def test_param_data(basic_param_data):
    assert basic_param_data in some_list


@pytest.mark.xfail(reason="failing on purpose")
def test_param_data_bad(basic_param_data):
    assert basic_param_data not in some_list

# https://docs.python.org/3/tutorial/modules.html for more info

# ---------------------------------------------------------------------------------------------------------------------
#                                             temp files notes
import os
import tempfile

import pytest


def read_data_from_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


@pytest.fixture
def temporary_file_with_data():
    """temporary file writing and reading """
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp_file.write("This is some data string")
    temp_file.close()

    yield temp_file.name

    os.unlink(temp_file.name)


def test_read_data_from_temp_file(temporary_file_with_data):
    data = read_data_from_file(temporary_file_with_data)
    assert data == "This is some data string"


@pytest.fixture
def temporary_file(request):
    """Temporary file (with params) - with addfinalizer (old style!)"""

    def create_temp_file(file_extension: str):
        temp_file = tempfile.NamedTemporaryFile(suffix=file_extension)
        request.addfinalizer(temp_file.close)
        return temp_file.name

    return create_temp_file


def test_file_operations(temporary_file):
    my_ext = ".txt"
    file_path = temporary_file(my_ext)
    assert file_path.endswith(my_ext)


#----------------------------------------------------------------------------------------------------------------------


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    for k in my_range(2, 13, 2):
        print(f"{k=}")
