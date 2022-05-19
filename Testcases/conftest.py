import pytest
import selenium
from selenium import webdriver


### pytest -v -s Testcases/test_login.py --browser chrome
### gives unbound local error on not providing the browser name while runtime if default broser name is mentioned in else part
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome("C://Users//user//chromedriver.exe")
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    elif browser == "IE":
        driver = webdriver.Ie()

    else:
        driver = webdriver.chrome()
    return driver



def pytest_addoption(parser):  ## this will get the value from CLI /hooks.
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):   ## this will return the browser value to setup method.
    return request.config.getoption("--browser")



###################  To generate pytest HTML report  ##############################

## it is hook for adding environment info to  HTML report

def pytest_configure(config):
    config._metadata['Project name'] = "nop commerce"
    config._metadata['Module name'] = "Customers"
    config._metadata['Tester'] = "Jadav"



## it is a hook to delete/modify environment info to HTML reports.

#@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



