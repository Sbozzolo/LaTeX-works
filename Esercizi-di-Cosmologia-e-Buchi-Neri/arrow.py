#!/usr/bin/python3

x0 = 0.2
x1 = 5
n = 10
delta = (x1 - x0)/n
spc = delta/4

def f(x):
    return 1/x

for i in range(n):
    x = x0 + i*delta
    print("\draw[->] (axis cs: ", round(x,2), ", ", round(f(x),2),") -- (axis cs: ",
          round(x + spc, 2), ", ", round(f(x + spc),2),");")
