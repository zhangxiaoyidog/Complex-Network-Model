# coding=utf-8

import sys
import matplotlib.pyplot as plt

import aver_shpathl
import random
import copy

import numpy as np

# 模拟attack
reload(sys)
sys.setdefaultencoding('utf8')
import webmodel

def getfloyd(namemat):
    lenthmat = copy.deepcopy(namemat)
    Num=len(lenthmat)
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
    return lenthmat


def largestsubgraph(flagg):
    namemat = []
    namemat = webmodel.readArff('E:/write.xls', flagg)
    Num = namemat.__len__()  # 节点个数
    scatterpr = []
    scatterpi = []
    Degreedis = []
    tempa=[]
    tempb = []
    largesta=[]
    largestb=[]
    for i in range(0,64):
        largesta.append(0)
        largestb.append(0)
    aa = copy.deepcopy(namemat)
    bb = copy.deepcopy(namemat)
    Num = namemat.__len__()
    for line in namemat:
        Degreedis.append(sum(line))
    #print Degreedis


    # intentional_attack后
    tempa = getfloyd(aa)
    print tempa
    k = 0
    for line in tempa:
        for j in line:

            if j != 0 and j != 'INF':
                largesta[k] += 1
        k += 1
    terma = max(largesta)
    scatterpi.append(terma)
    print terma

    for j in range(0, Num):
        k = 0
        for i in range(0, 63):
            largesta[i]=0
        maxnode = Degreedis.index(max(Degreedis))
        Degreedis[maxnode] = 0
        for m in range(0, Num):
            aa[m][maxnode] = 0
            aa[maxnode][m] = 0
        tempa=getfloyd(aa)
        for line in tempa:
            for j in line:
                if j!=0 and j!='INF':
                    largesta[k]+=1
            k+=1
        terma=max(largesta)
        scatterpi.append(terma)
    # random_attack后
    tempb = getfloyd(bb)
    k = 0
    for line in tempb:
        for j in line:
            if j != 0 and j != 'INF':
                largestb[k] += 1
        k += 1
    termb = max(largestb)
    scatterpr.append(termb)

    b_list = range(0, 63)
    blist_webId = random.sample(b_list, 63)
    for j in range(0, Num):
        k = 0
        for i in range(0, 63):
            largestb[i]=0
        temp = blist_webId[j]
        for m in range(0, Num):
            bb[m][temp] = 0
            bb[temp][m] = 0
        tempb = getfloyd(bb)
        for line in tempb:
            for j in line:
                if j != 0 and j != 'INF':
                    largestb[k] += 1
            k += 1
        termb = max(largestb)
        scatterpr.append(termb)

    print scatterpi
    print scatterpr
    x = np.arange(0, 64)
    y = x
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('Attack!!!')
    # 设置X轴标签
    plt.xlabel('Number')
    # 设置Y轴标签
    plt.ylabel('Maximum Connected Subgraph')
    # 画散点图
    ax1.scatter(x, scatterpi, s=12, c='r', marker='o')
    ax1.scatter(x, scatterpr, s=10, c='b', marker='o')
    # 设置图标
    label = ["intentional", "random"]
    plt.legend(label, loc=0, ncol=2)
    # 显示所画的图
    plt.show()


def aver_pathle(flagg):

    namemat = []
    namemat = webmodel.readArff('E:/write.xls', flagg)
    Num = namemat.__len__()  # 节点个数

    scatterpr = []
    scatterpi = []
    Degreedis = []
    Num = namemat.__len__()
    aa = copy.deepcopy(namemat)
    bb = copy.deepcopy(namemat)
    for line in namemat:
        Degreedis.append(sum(line))

    # intentional_attack后
    ava = aver_shpathl.calculation(bb, Num)
    scatterpi.append(ava)
    jin = Num
    for j in range(0, Num):
        maxnode = Degreedis.index(max(Degreedis))
        Degreedis[maxnode] = 0
        for k in range(0, Num):
            aa[k][maxnode] = 0
            aa[maxnode][k] = 0
        jin -= 1
        if jin == 0 or jin == 1:
            scatterpi.append(0)
        else:
            ave = aver_shpathl.calculation(bb, jin)
            scatterpi.append(ave)

    # random_attack后
    b_list = range(0, 63)
    blist_webId = random.sample(b_list, 63)
    ave = aver_shpathl.calculation(bb, Num)
    scatterpr.append(ave)

    jim = Num
    for j in range(0, Num):
        temp = blist_webId[j]
        for k in range(0, Num):
            bb[k][temp] = 0
            bb[temp][k] = 0
        jim -= 1
        if jim == 0 or jim == 1:
            scatterpr.append(0)
        else:
            ave = aver_shpathl.calculation(bb, jim)
            scatterpr.append(ave)
    x = np.arange(0, 64)
    y = x
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('Attack!!!')
    # 设置X轴标签
    plt.xlabel('Number')
    # 设置Y轴标签
    plt.ylabel('Average Path Length')
    # 画散点图
    ax1.scatter(x, scatterpi,s=12, c='r', marker='o')
    ax1.scatter(x, scatterpr,s=10, c='b', marker='o')
    # 设置图标
    label = ["intentional", "random"]
    plt.legend(label, loc=0, ncol=2)
    # 显示所画的图
    plt.show()


if __name__ == '__main__':
    largestsubgraph(0)
    aver_pathle(0)
