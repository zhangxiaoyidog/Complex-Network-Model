# coding=utf-8

import sys

# 计算节点和整个图的coreness
reload(sys)
sys.setdefaultencoding('utf8')
import webmodel

def corenessca(flagg):
    namemat = []
    coreness = []
    Degreedis = []
    namemat = webmodel.readArff('E:/write.xls',flagg)
    Num = namemat.__len__()  # 节点个数
    print namemat
    for i in range(0, Num):
        coreness.append(0)
        Degreedis.append(0)
    flag = 0
    while flag < 63:
        v = 0
        for line in namemat:
            Degreedis[v] = sum(line)
            v += 1
        for j in range(0, Num):
            if Degreedis[j] == flag:
                print('Number %d node has coreness: ' % (j + 1) ,flag)
                #print flag
                for k in range(0, Num):
                    namemat[k][j] = 0
                    namemat[j][k] = 0
        v = 0
        for line in namemat:
            Degreedis[v] = sum(line)
            v += 1
        flag2 = 0
        for l in range(0, Num):
            if Degreedis[l] == flag and flag!=0:
                flag2 = 1
        if flag2 == 0:
            flag += 1


if __name__ == '__main__':
    corenessca(2)

