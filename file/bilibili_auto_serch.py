from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extension.android.nativekey import AndroidKey

desired_caps = {
    'platformName' : 'Android', #检查设备标识
    'platforVersion' : '12', #手机安卓版本
    'deviceName' : 'fae1742e',
    'appPackage' : 'tv.danmaku.bili',
    'appActivity' : 'tv.danmaku.bili.MainActivityV2',
    'unicodeKeyboard' : True,#使用自带输入法
    'resetKeyboard' : True,#执行完程序恢复原理输入法
    'noReset' : True,#不要重置App
    'newCommandTimeout' : 6000,
    'automationName' : 'UiAutomator2'
}
# 连接Appium Server ,初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 如果有‘青少年保护’界面,点击‘我知道了’
iknow = driver.find_elements(By.ID, "text3")
if iknow:
    iknow.click()

# 根据ID定位搜索框,点击
sbox = driver.find_element(By.ID,'search_src_text')
sbox.send_keys('自动化测试'

# 输入回车键,确定搜索
driver.press_keycode(AndroidKey.ENTER)

# 选择(定位)所以视频标题
eles = driver.find_elements(By.ID,'title')

 
for ele in else:
    # 打印标题
    print(ele.text)
sleep(10)
driver.quit()

