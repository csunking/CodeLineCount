import os
# import string

path = "D:/WorkArts/ZJECMS/DBFSR/DataAnalysis/TidalFlow/FlowVec/"
dir = os.listdir(path)

def count(file):
    total = 0 #总行数
    countPound = 0 #注释行数
    countBlank = 0 #空行数
    line = open(file,'r', encoding='ISO-8859-1') # encoding='utf-8'打开文件，因为注释有中文所以使用utf-8编码打开
    for li in line.readlines(): #readlines()一次性读完整个文件
        total += 1
        if not li.split(): #判断是否为空行
            countBlank +=1
        li.strip()
        if li.startswith('#'):
            countPound += 1
    print(file)
    print("countBlank:%d" % countBlank)
    print("countPound:%d" % countPound)
    print("total:%d" % total)

for file in dir:
    count(path + file)