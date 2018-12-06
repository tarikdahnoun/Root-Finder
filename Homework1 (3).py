#Homework 1
#Tarik Dahnoun

import numpy as np
import pylab

def function(k,g,v0,t):
    A=-g*t/k + ((v0+g/k)/k)*(1-np.exp(-k*t))
    return A

def root_finder(a,b,k,g,v0):
    c=(a+b)/2
    
    while np.absolute(a-b)>=.0001:
        if np.sign(function(k,g,v0,c))==np.sign(function(k,g,v0,a)):
            a=c
        elif np.sign(function(k,g,v0,c))==np.sign(function(k,g,v0,b)):
            b=c
        c=(a+b)/2
        # print a,b,c
    return a,b,c
    
a1=2
b1=10.0

a2=3
b2=15.0

a3=4
b3=20.0

k=.02
g=9.8
v0=35.0
A1=root_finder(a1,b1,k,g,v0)
A2=root_finder(a2,b2,k,g,v0)
A3=root_finder(a3,b3,k,g,v0)
print A1

tmin=a1
tmax=b1
nts=100
ti=np.linspace(tmin,tmax,nts)
y=function(k,g,v0,ti)

pylab.plot(ti,y,'.',label=r"Landing time at Verticle Line, $\beta$="+"{}".format(k))
pylab.xlabel("Time [s]",fontsize=16)
pylab.ylabel("Position [m]",fontsize=16)
pylab.axhline(0,color='k',ls='--')
pylab.axvline(A1[0],color='k',ls='--',label=r"x=0")

pylab.title("Position with Drag")
pylab.show()

pylab.legend(loc='top',fontsize=11)