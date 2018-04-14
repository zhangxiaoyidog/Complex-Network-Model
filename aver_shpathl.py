# coding=utf-8

import sys


reload(sys)
sys.setdefaultencoding('utf8')
import webmodel
import copy

def calculationtwo(flag):
    lenthma = []
    lenthma = webmodel.readArff('E:/write.xls',flag)
    Num = lenthma.__len__()  # 节点个数
    lenthmat=copy.deepcopy(lenthma)
    for m in range(0,Num):
        for n in range(0, Num):
            if lenthmat[m][n]==0:
                lenthmat[m][n]='INF'
    for m in range(0, Num):
        lenthmat[m][m]=0

    for k in range(0,Num):
        for i in range(0, Num):
            for j in range(0, Num):
                if lenthmat[i][k] != 'INF' and lenthmat[k][j] != 'INF':
                    if lenthmat[i][j] > lenthmat[i][k] + lenthmat[k][j]:
                        lenthmat[i][j] = lenthmat[i][k] + lenthmat[k][j]
    sumlen=0
    for i in range(0,Num):
        for j in range(0,Num):
            if lenthmat[i][j]!='INF':
                sumlen = sumlen + lenthmat[i][j]
    ave=sumlen/1.0/(Num*(Num-1))
    print("aver_path lengh:", ave)
    return ave


def calculation(lenthma, Num):
    lenthmat=copy.deepcopy(lenthma)
    for m in range(0,Num):
        for n in range(0, Num):
            if lenthmat[m][n]==0:
                lenthmat[m][n]='INF'
    for m in range(0, Num):
        lenthmat[m][m]=0

    for k in range(0,Num):
        for i in range(0, Num):
            for j in range(0, Num):
                if lenthmat[i][k] != 'INF' and lenthmat[k][j] != 'INF':
                    if lenthmat[i][j] > lenthmat[i][k] + lenthmat[k][j]:
                        lenthmat[i][j] = lenthmat[i][k] + lenthmat[k][j]

    sumlen=0

    for i in range(0,Num):
        for j in range(0,Num):
            if lenthmat[i][j]!='INF':
                sumlen = sumlen + lenthmat[i][j]
    ave=sumlen/1.0/(Num*(Num-1))
    return ave


if __name__ == '__main__':
    lenthmat = []
    lenthmat = webmodel.readArff('E:/write.xls',0)
    Num = lenthmat.__len__()#节点个数
    #print namemat
    print Num
    #a = [[0, 1, 1, 0, 1], [1, 0, 1, 1, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
   # n=a.__len__()
    ave=calculation(lenthmat, Num)
    print("aver_path lengh:", ave)

