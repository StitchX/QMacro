from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pytest

wd = webdriver.Chrome()

@pytest.mark.usefixtures('login')
class TestDemo:
    @pytest.fixture(scope='class')
    def login(self):
        try:
            wd.get("https://www.qmacro.cn/app/#/post")
            wd.set_window_size(width='600', height='900')
            img1 = wd.get_screenshot_as_png()
            with open("../log/首页.png", "wb") as f:
                f.write(img1)

            search = wd.find_element(by='xpath', value='//*[@id="app"]/div/div[1]/div/div/div/div[3]/div')
            search.click()
        except:
            print('浏览器或网页打开失败')
        yield
        wd.quit()

    # @pytest.mark.usefixtures('login')
    def test_search(self):
        # search = wd.find_element(by='xpath', value='//*[@id="app"]/div/div[1]/div/div/div/div[3]/div')
        # search.click()
        query = wd.find_element(by='xpath',
                                value='//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div[2]/div/input')
        query.send_keys('Qmacro')
        query.send_keys(Keys.ENTER)
        # time.sleep(1)
        img2 = wd.get_screenshot_as_png()
        with open('../log/搜索.png', 'wb') as f:
            f.write(img2)

    # @pytest.mark.usefixtures('login')
    def test_search_long(self):

        query = wd.find_element(by='xpath',
                                value='//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div[2]/div/input')

        query.clear()
        time.sleep(1)
        query.send_keys('好好好好好好')
        time.sleep(2)
        query.send_keys(Keys.ENTER)
        time.sleep(1)
        img2 = wd.get_screenshot_as_png()
        with open('../log/搜索_长.png', 'wb') as f:
            f.write(img2)

