from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

wd = webdriver.Chrome()
wd.get("https://www.qmacro.cn/app/#/post")
# wd.implicitly_wait(5)
wd.set_window_size(width='600',height='900')
# time.sleep(2)

time.sleep(2)
img1=wd.get_screenshot_as_png()
with open("../log/首页.png","wb") as f:
    f.write(img1)


wd.quit()