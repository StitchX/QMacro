import time

import pytest
from selenium import webdriver
import pytest

wd = webdriver.Chrome()

@pytest.mark.usefixtures('login')
class TestDemo():
    @pytest.fixture(scope='class')
    def login(self):
        try:
            # 打开网站
            wd.get("https://www.qmacro.cn/app/#/post")
            wd.set_window_size(width='600', height='900')
            time.sleep(1)
        except:
            print('')
        yield
        # 关闭浏览器
        wd.quit()

    # 打开系统公告
    def test_xxgg(self):
        xtgg = wd.find_element(by='xpath',
                        value='//*[@id="app"]/div/div[2]/div/div/div[2]/section[1]/ul/li[1]/a/div/div/div/img')
        xtgg.click()
        time.sleep(1)
        # 回到首页
        back = wd.find_element(by='xpath',
                               value='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div[1]/div')
        time.sleep(2)
        back.click()
        time.sleep(1)

    # 打开和平精英
    def test_hpjy(self):
        xtgg = wd.find_element(by='xpath',
                        value='//*[@id="app"]/div/div[2]/div/div/div[2]/section[1]/ul/li[2]/a/div/div/div/img')
        xtgg.click()
        time.sleep(1)

        # 切换到【配置】列表
        peizhi = wd.find_element(by='xpath',
                                 value='//*[@id="app"]/div/div[2]/div[1]/div[1]/div/div[2]/span')
        peizhi.click()
        time.sleep(1)

        # 切换到【最新】列表
        zuixin = wd.find_element(by='xpath',
                                 value='//*[@id="app"]/div/div[2]/div[1]/div[1]/div/div[3]/span')
        zuixin.click()
        time.sleep(1)

        # 返回到【首页】
        back = wd.find_element(by='xpath',
                               value='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div[1]/div')
        back.click()
        time.sleep(1)

    # 打开【王者荣耀】
    def test_wzry(self):
        xtgg = wd.find_element(by='xpath',
                        value='//*[@id="app"]/div/div[2]/div/div/div[2]/section[1]/ul/li[3]/a/div/div/div/img')
        xtgg.click()
        time.sleep(1)

        # 切换到【配置】列表
        peizhi = wd.find_element(by='xpath',
                                 value='//*[@id="app"]/div/div[2]/div[1]/div[1]/div/div[2]/span')
        peizhi.click()
        time.sleep(1)

        # 切换到【最新】列表
        zuixin = wd.find_element(by='xpath',
                                 value='//*[@id="app"]/div/div[2]/div[1]/div[1]/div/div[3]/span')
        zuixin.click()
        time.sleep(1)

        # 返回到【首页】
        back = wd.find_element(by='xpath',
                               value='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div[1]/div')
        back.click()
        time.sleep(1)


if __name__ == '__main__':
    pytest.main(['test_difClass.py::TestDemo'])