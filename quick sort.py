import datetime
from numpy import random

def partition(a,l,u):
    pivot=a[l]
    start=l+1
    end=u
    while True:
        while start<=end and a[start]<=pivot:
            start+=1
        while start<=end and a[end]>pivot:
            end-=1
        if start<=end:
            a[start],a[end] = a[end],a[start]
        else:
            break
    a[l],a[end] = a[end],a[l]
    return end

def quick_sort(a,l,u):
    if l<u:
        loc=partition(a,l,u)
        quick_sort(a,l,loc-1)
        quick_sort(a,loc+1,u)

a=[]
for i in range(1000):
   a.append(random.randint(500))
x=datetime.datetime.now()
quick_sort(a,0,len(a)-1)
y=datetime.datetime.now()
c=y-x
print(c)
print(a)
