import datetime
a=[]
for i in range(100):
    a.append(i)
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
