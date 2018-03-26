# -*- coding: utf-8 -*-
import csv,codecs
import pandas as pd
import os

def fuck_douhao(n):
    if n != ',':
        return n

if __name__ == '__main__':

    # 定义数组
    read_csv = []
    write_csv = []
    file_list = []
    file_path = input("输入路径：")
    file_class = input("选择导入的项目 1:讲堂  2:思政：")
    file_format = input("输入要查找的格式：")
    text_start_row = input("真正的数据是第几行:")
    x = 0
    sheet_name = 0
    rows_array = []
    rows_count = 0
    key_word = ''
    title_jt = ['Id', 'Name', 'Class', 'Department', 'State', 'Date']
    title_sz = ['AcademicYear', 'Semester', 'Id', 'Name', 'Credit', 'Score', 'CourseId', 'CourseName', 'CourseNature',
                'CommencementInstitute', 'Institute', 'Class']
    # 简写os.path.splitext
    data_easy_os = os.path.splitext
    # 定义关键字
    if int(file_class) == 1:
        key_word = '讲'
        # print('设置为讲')
    elif int(file_class) == 2:
        key_word = '思'
        # print('设置为思')
    else:
        key_word = '未定义'
    # 文件路径设置
    for root, dirs, files in os.walk(file_path):
        for file in files:
            # os.path.splitext将路径分为两部分：路径文件+后缀
            if data_easy_os(file)[1] == '.' + file_format:
                file_list.append(os.path.join(root, file))
    # 遍历文件
    for file_name in file_list:
        # 按关键字搜索表
        if file_name.find(key_word) != -1:
            data_read_xls = pd.read_excel(file_name, sheet_name, index_col=0)
            data_read_xls.to_csv(data_easy_os(file_name)[0] + '(read)' + '.csv', encoding='utf-8')
            with open(data_easy_os(file_name)[0] + "(read)" + ".csv", 'r', encoding='utf-8') as read_csv:
                reader = csv.reader(read_csv)
                rows = [row for row in reader]
                # 当前库都在同一文件夹内，导致xls文件过多，影响使用，所以放入数组只取array中的第一个rows
                rows_array.insert(rows_count, rows)
                rows_count = rows_count + 1
        else:
            continue
        # 删除第一行标题
        del rows[0:int(text_start_row) - 1]
        # 在第一行插入一个新的标题
        if int(file_class) == 1:
            rows_array[0].insert(0, title_jt)
        else:
            rows_array[0].insert(0, title_sz)
        # 写入csv文件
        if rows_array[0] == rows:
            # newline=''消除了空行 (utf_8_sig 是utf-8 BOM格式) (utf_8 是utf-8无BOM格式)
            with codecs.open(os.path.splitext(file_name)[0] + "(write)" + ".csv", 'w', 'utf_8') as write_csv:
                write = csv.writer(write_csv, dialect='excel')
                for index, value in enumerate(rows_array[0]):
                    for val in enumerate(value):
                    	#过滤空内容项
                        newlist = filter(fuck_douhao, value)
                    write.writerow(newlist)
        else:
            print('错误')
