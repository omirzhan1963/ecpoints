# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:47:52 2019

@author: Bilim
"""
def dfile(fname):
    f=open(fname,"r")
    lines=f.readlines()
    l=[]
    for k in lines:
        ik=int(k)
        l.append(ik)
    return l
def compl(l1,l2):
    l=l1+l2
    l.sort()
    i=0
    r=False
    for k in l:
        if k==i:
            r=True
            print("ooo")
        i=k
    return r
l1=dfile("x.txt")
l2=dfile("testx.txt")
print(compl(l1,l2))