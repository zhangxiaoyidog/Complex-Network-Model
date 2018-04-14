# coding=utf-8

import sys

#计算E[i],C[i]后使用公式计算cluster
reload(sys)
sys.setdefaultencoding('utf8')
import webmodel

def getclustering_co(flag):
    namemat = []
    EEE = []
    CCC = []

    namemat = webmodel.readArff('E:/write.xls', flag)
    Num = namemat.__len__()  # 节点个数
    # print namemat
    #print Num

    for i in range(0, 63):
        EEE.append(0)
        CCC.append(0)
    for i in range(0, 63):
        neighbornum = 0
        neighbor = []
        for j in range(0, 63):
            if i != j and namemat[i][j] == 1:
                neighbornum += 1
                neighbor.append(j)
        for linea in neighbor:
            for lineb in neighbor:
                if namemat[linea][lineb] == 1:
                    EEE[i] += 1
        EEE[i] = EEE[i] / 2
        # print EEE[i]
        if (EEE[i] == 0):
            CCC[i] = 0
        else:
            CCC[i] = 2 * EEE[i] / 1.0 / (neighbornum * (neighbornum - 1))
    aver = sum(CCC) / 1.0 / Num
    print aver

if __name__ == '__main__':
    getclustering_co(0)