import numpy as np
a=np.random.randint(10000,size=10000)
import datetime
x=datetime.datetime.now()
for i in range(1,len(a)):
    temp=a[i]
    for j in range(i-1,-1,-1):
        if temp<a[j]:
            a[j],a[j+1]=a[j+1],a[j]
b=datetime.datetime.now()
c=b-x
print(c)

for e in a:
    print(e,end=" ")
