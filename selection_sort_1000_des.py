import datetime
a=[]
for i in range(999,-1,-1):
    a.append(i)
x=datetime.datetime.now()
for i in range(len(a)):
    min=a[i]
    globals()['pos']=i
    for j in range(i+1,len(a)):
        if min>a[j]:
            min=a[j]
            globals()['pos']=j
    t=a[i]
    a[i]=a[pos]
    a[pos]=t
b=datetime.datetime.now()
c=b-x
print(c)

for e in a:
    print(e,end=' ')
