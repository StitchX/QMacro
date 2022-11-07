from selenium import webdriver
import pytest
import time

@pytest.fixture()
def login():
    wd = webdriver.Chrome()
    try:
        wd.get("https://www.qmacro.cn/app/#/post")
        time.sleep(1)
    except:
        print('')
    yield
    wd.quit()