# coding=utf-8
from Tkinter import *
import easygui
import netgraph
import degree_dis
import aver_shpathl
import clustering_co
import coreness_ca
import random_attack
import matplotlib.pyplot as plt


root = Tk()
root.title('welcome! ! !')
root.geometry('500x400+500+300')
v = IntVar()


def callback():
    if (str(var.get()) == '1'):
        netgraph.drawnetgraph(0)

    if (str(var.get()) == '2'):
        netgraph.drawnetgraph(1)

    if (str(var.get()) == '3'):
        netgraph.drawnetgraph(2)


def callbackone():
    if (str(var.get()) == '1'):
        degree_dis.showdegree(0)

    if (str(var.get()) == '2'):
        degree_dis.showdegree(1)

    if (str(var.get()) == '3'):
        degree_dis.showdegree(2)


def callbacktwo():
    if (str(var.get()) == '1'):
        degree_dis.showdistribution(0)

    if (str(var.get()) == '2'):
        degree_dis.showdistribution(1)

    if (str(var.get()) == '3'):
        degree_dis.showdistribution(2)


def callbackaver():
    if (str(var.get()) == '1'):
        aver_shpathl.calculationtwo(0)

    if (str(var.get()) == '2'):
        aver_shpathl.calculationtwo(1)

    if (str(var.get()) == '3'):
        aver_shpathl.calculationtwo(2)


def callbackclustering():
    if (str(var.get()) == '1'):
        clustering_co.getclustering_co(0)

    if (str(var.get()) == '2'):
        clustering_co.getclustering_co(1)

    if (str(var.get()) == '3'):
        clustering_co.getclustering_co(2)


def callbackcoreness():
    if (str(var.get()) == '1'):
        coreness_ca.corenessca(0)

    if (str(var.get()) == '2'):
        coreness_ca.corenessca(1)

    if (str(var.get()) == '3'):
        coreness_ca.corenessca(2)


def callbacklargestgraph():
    if (str(var.get()) == '1'):
        random_attack.largestsubgraph(0)

    if (str(var.get()) == '2'):
        random_attack.largestsubgraph(1)

    if (str(var.get()) == '3'):
        random_attack.largestsubgraph(2)


def attack_averpathl():
    if (str(var.get()) == '1'):
        random_attack.aver_pathle(0)

    if (str(var.get()) == '2'):
        random_attack.aver_pathle(1)

    if (str(var.get()) == '3'):
        random_attack.aver_pathle(2)


group = LabelFrame(root, text='welcome!')  # 基于root 制定一个框架 .
group.pack(padx=50)

var = IntVar()
R1 = Radiobutton(root, text="name", variable=var, value=1, )
R1.pack(anchor=W)

R2 = Radiobutton(root, text="hometown", variable=var, value=2)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="dialect", variable=var, value=3)
R3.pack(anchor=W)
webgraphButton = Button(root, text='显示网络图', command=callback)

webgraphButton.pack(pady=0)

nodedisButton = Button(root, text='node degree show', command=callbackone)
nodedisButton.pack(pady=0)

nodedisButton2 = Button(root, text='node-de_distribution ', command=callbacktwo)
nodedisButton2.pack(pady=0)

getaverpath = Button(root, text='aver_shpathlength ', command=callbackaver)
getaverpath.pack(pady=0)

clustering = Button(root, text='clustering_coefficient ', command=callbackclustering)
clustering.pack(pady=0)

coreness = Button(root, text='coreness ', command=callbackcoreness)
coreness.pack(pady=0)

attack_largestgraph = Button(root, text='attack_largestgraph ', command=callbacklargestgraph)
attack_largestgraph.pack(pady=0)

attack_averpathl = Button(root, text='attack_averpathlength ', command=attack_averpathl)
attack_averpathl.pack(pady=0)

mainloop()
