# -*- coding: utf-8 -*-
import csv
import os
import pandas as pd

# 定义数组
read_csv = []
write_csv = []
file_list = []
file_path = input("输入路径：")
file_format = input("输入要查找的格式：")
text_start_row = input("真正的数据是第几行:")
# 简写os.path.splitext
data_easy_os = os.path.splitext
for root, files in os.walk(file_path):
    for file in files:
        # os.path.splitext将路径分为两部分：路径文件+后缀
        if data_easy_os(file)[1] == '.' + file_format:
            file_list.append(os.path.join(root, file))
for file_name in file_list:
    data_read_xls = pd.read_excel(file_name, 'Sheet1', index_col=0)
    data_read_xls.to_csv(data_easy_os(file_name)[0] + '(read)' + '.csv', encoding='utf-8')
    with open(data_easy_os(file_name)[0] + "(read)" + ".csv", 'r', encoding='utf-8') as read_csv:
        reader = csv.reader(read_csv)
        rows = [row for row in reader]
    del rows[0:int(text_start_row) - 1]
    title = ['Id', 'Name', 'Class', 'Department', 'State', 'Date']
    rows.insert(0, title)
    # newline=''消除了空行
    with open(os.path.splitext(file_name)[0] + "(write)" + ".csv", 'w', newline='') as write_csv:
        write = csv.writer(write_csv, dialect='excel')
        for mtuple in rows:
            write.writerow(mtuple)
