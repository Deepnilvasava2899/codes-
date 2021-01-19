import datetime
a=[]
for i in range(100):
    a.append(i)
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
