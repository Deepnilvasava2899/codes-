def count_sort(a):
    temp=[0]*len(a)
    count=[0]*10

    for i in range(len(a)):
        count[a[i]]+=1

    for i in range(1,len(count)):
        count[i]+=count[i-1]

    i=len(a)-1
    while i>=0:
        count[a[i]]-=1
        temp[count[a[i]]]=a[i]
        i-=1

    for i in range(len(a)):
        a[i]=temp[i]
    
a=[1,4,5,7,8,4,1,3,9,5,3,1,2,4,9,8,5,6]
count_sort(a)
print(a)
