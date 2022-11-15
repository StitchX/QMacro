import time
import pytest
from selenium import webdriver

wd = webdriver.Chrome()
@pytest.fixture(scope='class')
def login():
    # wd = webdriver.Chrome()
    try:
        wd.get("https://www.qmacro.cn/app/#/post")
        wd.set_window_size(width='600', height='900')
        img1 = wd.get_screenshot_as_png()
        with open("../log/首页.png", "wb") as f:
            f.write(img1)
        wd.implicitly_wait(10)
    except:
        print('')
    # yield wd.close()