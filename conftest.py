import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.get(Urls.MAIN_PAGE)
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()