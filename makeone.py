denominator =[7,5,4,1]
size =len(denominator)#the len is 4 ass we have given

def findMin(value):
    arr=[0]
    ans=[]
    for i in range(0,size,1):#this is where the denominator will run as loop
        while value >= denominator[i]:
            value=value-denominator[i]
            print(value)
            ans.append(denominator[i])
    print(ans)
    print("left",value)
n=41
findMin(n)
