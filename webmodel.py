# -*- coding: utf-8 -*-
import xlrd
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

def readArff(fileName,Num):
    aa = []
    bb = []
    data = xlrd.open_workbook('E:/write.xls')
    table = data.sheets()[Num]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    for i in xrange(0, nrows):
        if i == 0:
            continue
        rowValues = table.row_values(i)  # 某一行数据
        # print rowValues
        j = 0
        for item in rowValues:
            a = item.encode("utf-8")
            if a != 'm' and a != 'y' and a != 'n':
                continue
            if a == 'm' or a == 'n':
                bb.append(0)
            if a == 'y':
                bb.append(1)
            j += 1
        aa.append(bb)
        bb = []
    return aa

