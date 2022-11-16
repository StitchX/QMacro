import time
import pytest
from selenium import webdriver

wd = webdriver.Chrome()
@pytest.fixture(scope='class')
def login():
    try:
        wd.get("https://www.qmacro.cn/app/#/post")
        time.sleep(1)
        wd.set_window_size(width='600', height='900')
        img1 = wd.get_screenshot_as_png()
        with open("../log/首页.png", "wb") as f:
            f.write(img1)
    except:
        print('页面打开失败')