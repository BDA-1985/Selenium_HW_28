from selenium import webdriver
import pytest
import settings


@pytest.fixture()
def browser():
    browser = webdriver.Chrome('C:\\Users\\user\\Desktop\\ALF\\Skillfactory\\chromedriver.exe')
    browser.get(settings.BASE_URL)

    yield browser
    browser.quit()
