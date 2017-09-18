import os
from openpyxl import Workbook
from os.path import join
import getVideoLength
import WriteExcel
from openpyxl import load_workbook

root_dir = "D:\WDS\分享的所有文件\\008_UBOOT移植_LINUX移植_驱动移植"
column = 'E'
count = 6
wb = load_workbook(filename='sample.xlsx')
ws = wb['Sheet']

for root, dirs, files in os.walk(root_dir):
    for a in (join(root, name) for name in files):
        if a.endswith('.WMV'):
            # print(a)
            count += 1
            data = getVideoLength.getLenTime(a)
            data = float(data)
            min = int(data / 60)
            sec = int(data - min * 60)
            if(sec < 10):
                sec = "0" + str(sec)
            length = str(min) + ":" + str(sec)
            data = a.split('\\')[-1]
            WriteExcel.WriteExcelPos(column, str(count), length, ws)
            WriteExcel.WriteExcelPos('D', str(count), data, ws)

wb.save("sample.xlsx")