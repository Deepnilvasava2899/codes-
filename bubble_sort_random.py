import numpy as np
import datetime
a=np.random.randint(10000,size=10000)
x=datetime.datetime.now()
for k in range(len(a)):
    for i in range(k,len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
b=datetime.datetime.now()
c=b-x
print(c)

for e in a:
    print(e,end=' ')
