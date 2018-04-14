# coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf8')
import webmodel
import matplotlib.pyplot as plt
from matplotlib.font_manager import *
from matplotlib import mlab
from matplotlib import rcParams


def showdegree(flag):
    namemat = []
    Degreedis = []
    namemat = webmodel.readArff('E:/write.xls', flag)
    Num = namemat.__len__()  # 节点个数
    for i in range(0, 63):
        Degreedis.append(0)
    i = 0
    for line in namemat:
        Degreedis[i] = sum(line)
        i += 1
    # print Degreedis
    temp = []

    for j in range(0, 63):
        temp.append(j)
    fig1 = plt.figure(2)
    rects = plt.bar(left=(temp[0:63]), height=(Degreedis[0:63]), width=1, align="center", yerr=0.000001)
    plt.title('The degree of these nodes')
    plt.xlabel('Number of nodes')
    plt.ylabel('Degree')
    plt.show()

def showdistribution(flag):
    namemat = []
    Degreedis = []
    namemat = webmodel.readArff('E:/write.xls', flag)
    Num = namemat.__len__()  # 节点个数
    for i in range(0, 63):
        Degreedis.append(0)
    i = 0
    for line in namemat:
        Degreedis[i] = sum(line)
        i += 1
    # print Degreedis
    temp = []
    for j in range(0, 63):
        temp.append(j)
    aver_degree = sum(Degreedis) / Num
    M = max(Degreedis)  # 最大的度
    print M
    Degreedistribution = []
    dnum = []
    for m in range(0, M + 1):
        Degreedistribution.append(0)
        dnum.append(0)

    for item in Degreedis:
        for n in range(0, M + 1):
            if item == n:
                dnum[n] += 1
    for k in range(0, M + 1):
        Degreedistribution[k] = dnum[k] / 1.0 / Num
    fig1 = plt.figure(2)
    rects = plt.bar(left=(temp[0:M + 1]), height=(Degreedistribution[0:M + 1]), width=1, align="center", yerr=0.000001)
    plt.title('The degreedistribution of these nodes')
    plt.xlabel('Number of nodes')
    plt.ylabel('Degreedistribution')
    plt.show()


if __name__ == '__main__':
    showdegree(0)
    showdistribution(0)

