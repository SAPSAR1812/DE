import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def f(x,y):
    b=-x*x*y
    return b




def eulers():
    z=[0]*5
    h=0.5
    x=0
    i=0
    y=1
    while(True):
        z[i]=y
        i=i+1
        y=y+f(x,y)*h
        x=x+h
        if(x>2):
            return z
            break
def heuns():
    z=[0]*5
    h=0.5
    x=0
    i=0
    y=1
    while(True):
        z[i]=y
        i=i+1
        k=f(x,y)
        print(k)
        y=y+(k+f(x+h,y+k*h))*(h/2)
        x=x+h
        if(x>2):
            return z
            break

def ralstons():
    z=[0]*5
    h=0.5
    x=0
    i=0
    y=1
    while(True):
        z[i]=y
        k=f(x,y)
        y=y+((k/3)+((2/3)*f(x+0.75*h,y+0.75*k*h)))*(h)
        x=x+h
        i=i+1
        if(x>2):
            return z
            break
def fourRK():
    
    h=0.5
    x=0
    y=1
    i=0
    z=[0]*5
    while(True):
        z[i]=y
        k1=f(x,y)
        k2=f(x+(h/2),y+((k1*h)/2))
        k3=f(x+(h/2),y+((k2*h)/2))
        k4=f(x+(h),y+(k3*h))
        y=y+(k1+(2*k2)+(2*k3)+k4)*(h/6)
        x=x+h
        i=i+1
        if(x>2):
            return z
            break
L1=[0]*5
L2=eulers()
L3=heuns()
L4=ralstons()
L5=fourRK()
A=pd.DataFrame([L1,L2,L3,L4,L5],columns=['0','0.5','1','1.5','2'])

A.index=['Anaytical','Eulers','Heuns','Ralstons','Fourth Order RK']
print(A)


