# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import ecdsa
from datetime import datetime as dt
curvesec=ecdsa.curves.SECP256k1
curve=curvesec.curve
G=curvesec.generator
n=curvesec.order
co=curve.p()
co2=co//2
hprime=[]
h1prime=[1]
flastx="lastx.txt"
flasty="lasty.txt"
flastord="lastord.txt"
fx="x.txt"
ford="ord.txt"
k=2
i=0
while i<100:
    
    if ecdsa.numbertheory.is_prime(k):
        hprime.append(k)
        h1prime.append(k)
        i+=1
    k+=1

def inv(k):
    r=pow(k,(n-2),n)
    return r
invprime=[]
for i in range(100):
    k=hprime[i]
    r=inv(k)
    invprime.append(r)
def fromleft(p,ordp):
    desd=co-p.x()
    mind=co
    for i in range(10):
        pp=p*hprime[i]
        ordpp=(ordp*hprime[i])%n
        addd=abs(pp.x()-desd)
        if (pp.x()<co2) and (addd<mind):
            minp=pp
            minord=ordpp
            mind=addd
    if mind==co:
        for i in range(10,100):
            pp=p*hprime[i]
            ordpp=(ordp*hprime[i])%n

            if (pp.x()<co2):
                minp=pp
                minord=ordpp
    return minp,minord
def fromright(p,ordp):
    desd=co-p.x()
    mind=co
    for i in range(10):
        pp=p*invprime[i]
        ordpp=(ordp*invprime[i])%n
        addd=abs(pp.x()-desd)
        if (pp.x()>co2) and (addd<mind):
            minp=pp
            minord=ordpp
            mind=addd
    if mind==co:
        for i in range(10,100):
            pp=p*invprime[i]
            ordpp=(ordp*invprime[i])%n

            if (pp.x()>co2):
                minp=pp
                minord=ordpp
    return minp,minord
def minp(p,ordp,p1,ordp1):
    mind=co
    for k in h1prime:
        for l in h1prime:
            pp=p*k+p1*l
            ordpp=(ordp*k+ordp1*l)%n
            if pp.x()==p.x():
                continue
            if pp==ecdsa.ellipticcurve.INFINITY:
                continue
            if abs(pp.x()-co2)<mind:
                minp=pp
                minord=ordpp
                mind=abs(pp.x()-co2)
    return minp,minord
def findpoint(p,ordp):
    if p.x()>co2:
        k=fromleft(p,ordp)
    else:
        k=fromright(p,ordp)
    return minp(p,ordp,k[0],k[1])
def savelast(p,ordp):
    f=open(flastx,"w")
    f.write(str(p.x()))
    f.close()
    f=open(flasty,"w")
    f.write(str(p.y()))
    f.close()    
    f=open(flastord,"w")
    f.write(str(ordp))
    f.close()
def createlist(listlength):
    f=open(flastx,"r")
    x=f.read()
    x=int(x)
    f.close()
    f=open(flasty,"r")
    y=f.read()
    y=int(y)
    f.close()    
    f=open(flastord,"r")
    ordstr=f.read()
    ordp=int(ordstr)
    f.close()
    p=ecdsa.ellipticcurve.Point(curve,x,y)
    l=[]
    k=(p,ordp)
    for i in range(listlength):
        l.append((k[0].x(),k[1]))
        k=findpoint(k[0],k[1])
    
    f1=open(fx,"a")
    f2=open(ford,"a")    
    for i in range(listlength):
        str1=str(l[i][0])+"\n"
        f1.write(str1)
        str2=str(l[i][1])+"\n"
        f2.write(str2)
    f1.close()
    f2.close()
    savelast(k[0],k[1])        
def collectdata(listlength,repeattimes):
    for i in range(repeattimes):
        createlist(listlength)


#savelast(G,1)
print(dt.now())
collectdata(30,10)
print(dt.now())        
    

