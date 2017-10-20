# Excel转CSV

为什么写这个，因为：我懒得手动改了...

python也是刚刚开始学

总共用了3个模块

csv、os、pandas

os——操作文件

pandas——操作Excel文件

csv——操作csv文件

##这个实现的原理：

首先这个可以输入路径、要查找的格式、从第几行开始（我用的表涉及一个没用的表头问题，不需要的话可以删掉）

###1.选择路径

root 根目录 dirs 目录名 files 文件名

file_format（文件格式）

data_easy_os简化了操作命令

导入os模块

~~~~Python
import os
~~~~

```Python
# 简写os.path.splitext
data_easy_os = os.path.splitext
for root, dirs, files in os.walk(file_path):
for file in files:
    # os.path.splitext将路径分为两部分：路径文件+后缀
    if data_easy_os(file)[1] == '.' + file_format:
        file_list.append(os.path.join(root, file))
```
往file_list这个数组中添加文件路径

###2.读取Excel数据文件

需要导入pandas模块

~~~~Python
import pandas as pd
~~~~

pd 就是pandas

file_name（可输入的文件名）

```Python
for file_name in file_list:
data_read_xls = pd.read_excel(file_name, 'Sheet1', index_col=0)
```

###3.输出要读取的csv文件

拆分路径，形成名字+(read).csv文件

~~~~python
   data_read_xls.to_csv(data_easy_os(file_name)[0] + '(read)' + '.csv', encoding='utf-8')
~~~~

###4.读取csv文件并把数据放入数组

~~~~python
with open(data_easy_os(file_name)[0] + "(read)" + ".csv", 'r', encoding='utf-8') as read_csv:
        reader = csv.reader(read_csv)
        rows = [row for row in reader]
~~~~

###5.改数组

依个人需求，不需要可删

~~~~python
del rows[0:int(text_start_row) - 1]
    title = ['Id', 'Name', 'Class', 'Department', 'State', 'Date']
    rows.insert(0, title)
~~~~

###6.把数据放入一个新的csv文件

因为去的是数组，放入时会影响格式，mtuple取单项值，循环放入

~~~~Python
    # newline=''消除了空行
    with open(os.path.splitext(file_name)[0] + "(write)" + ".csv", 'w', newline='') as write_csv:
        write = csv.writer(write_csv, dialect='excel')
        for mtuple in rows:
            write.writerow(mtuple)
~~~~

:happy: