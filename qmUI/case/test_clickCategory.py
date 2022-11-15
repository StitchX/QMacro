import time
import pytest
import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wd = conftest.wd

@pytest.mark.usefixtures('login')
class TestDemo():

    dataCats = ('//*[@id="app"]/div/div[2]/div/div/div[2]/section[1]/ul/li[1]/a/div/div/div',
               '//*[@id="app"]/div/div[2]/div/div/div[2]/section[1]/ul/li[2]/a/div/div/div',
               '//*[@id="app"]/div/div[2]/div/div/div[2]/section[1]/ul/li[3]/a/div/div/div')
    @pytest.mark.parametrize('dataCat',dataCats)
    @pytest.mark.usefixtures('login')
    def test_demo(self,dataCat):
        global dataCats
        # category = WebDriverWait(wd,10,0.5).until(EC.visibility_of_element_located(by='xpath',
        #                     value=dataCat))

        category = wd.find_element(by='xpath',
                            value=dataCat)
        category.click()
        time.sleep(1)

        try:
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
        except:
            pass
        finally:
            # 回到首页
            back = wd.find_element(by='xpath',
                                   value='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div[1]/div')
            back.click()
            time.sleep(1)


if __name__ == '__main__':
    pytest.main(['test_difClass.py::TestDemo'])