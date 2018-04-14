# coding=utf-8
import networkx as nx
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import webmodel
import matplotlib.pyplot as plt


def drawnetgraph(Num):
    lenthmat = webmodel.readArff('E:/write.xls',Num)
    G = nx.Graph()
    Matrix = np.array([])
    Matrix = np.array(lenthmat)
    #print len(Matrix)
    for i in range(0,63):
        for j in range(0,63):
            if Matrix[i][j] == 1:
                G.add_edge(i, j)
    del lenthmat
    nx.draw(G, node_size=20)
    plt.show()


if __name__ == '__main__':
    drawnetgraph(1)
