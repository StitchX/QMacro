import time
from selenium.webdriver.common.keys import Keys
import pytest
from conftest import wd


@pytest.mark.usefixtures('login')
class TestSearch:
    @pytest.fixture(scope='class')
    def clickSearch(self):
        search = wd.find_element(by='xpath', value='//*[@id="app"]/div/div[1]/div/div/div/div[3]/div')
        search.click()


    @pytest.mark.parametrize("data", ['QMacro', '超长噢噢噢哈哈哈哈哈哈哈烦烦烦烦烦烦烦烦烦呱呱呱呱呱呱'])
    @pytest.mark.usefixtures('login','clickSearch')
    def test_search(self,data):
        query = wd.find_element(by='xpath',
                                value='//*[@id="app"]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div[2]/div/input')
        print(data)
        query.send_keys(data)
        query.send_keys(Keys.ENTER)
        time.sleep(1)
        img2 = wd.get_screenshot_as_png()
        with open('../log/'+data[0]+'搜索.png', 'wb') as f:
            f.write(img2)
        # 页面刷新，搜索内容重置
        wd.refresh()
        time.sleep(1)




