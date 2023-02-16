import os
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy



desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "12",
  "deviceName": "fae1742e",
  #com.android.settings/com.android.settings.MiuiSettings
  "appPackage": "com.android.settings",
  "appActivity": "com.android.settings.MiuiSettings",

  #"automationName":"uiautomator2",
  "noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
# 设置缺省等待时间
driver.implicitly_wait(5)

def fileRead():
  os.system("adb shell \"ps | grep com.xiaomi\" > C:\Users\ryazan\Desktopdesktop\ps.txt")
  file = open('desktop/ps.txt')
  line = file.readline().strip()
  txt = []
  txt.append(line)
  while line:
    line = file.readline().strip()
    txt.append(line)
  
  file.close()
  print(txt)

def __main__init__():
  fileRead()


#
# f=open('唐诗一百首.txt')
# line = f.readline().strip() #读取第一行
# txt=[]
# txt.append(line)
# while line:  # 直到读取完文件
#    line = f.readline().strip()  # 读取一行文件，包括换行符
#    txt.append(line)
# f.close()  # 关闭文件
# print(txt)


'''
# 屏幕从下向上滑动
times = 0
while times < 3:
  driver.swipe(500, 2050, 500, 900, 1000)
  times+=1
  
# 打开更多设置
searchCode = 'new UiSelector().text("更多设置")'
sbox = driver.find_element(
  AppiumBy.ANDROID_UIAUTOMATOR,searchCode
).click()

sleep(10)
driver.quit()
'''

