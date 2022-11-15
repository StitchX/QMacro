import time

from selenium import webdriver

def login():
    wd = webdriver.Chrome()
    try:
        wd.get("https://www.qmacro.cn/app/#/post")
        time.sleep(2)
    except:
        print('')
    yield wd.close()