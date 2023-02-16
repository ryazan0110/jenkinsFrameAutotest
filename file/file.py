import os
from time import sleep


def fileRead():
  #os.system("adb shell \"ps | grep com.xiaomi \" > ps.txt")
  file = open('ps.txt')
  line = file.readline().strip()
  txt = []
  txt.append(line)
  while line:
    line = file.readline().strip()
    txt.append(line)
  
  file.close()
  print(txt)

