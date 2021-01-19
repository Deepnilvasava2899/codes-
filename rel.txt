#the fucntion will be used to process the hash 
def pro_hash(x):
    answer=[]
    for i in x:
        pr=27
        m=100000
        hash_v=0
        pro_pow=1
        for j in i:
            hash_v=(hash_v + (ord(j)-ord('a')+1)*pro_pow)%m
            pro_pow=(pro_pow*pr)%m
        answer.append(hash_v)
    return answer

#this function is used for least common sequence algorithm


def LCS(x,y,lx,ly):
    if lx==0 or ly==0:                                  #terminating condition
        return 0
    elif x[lx-1] == y[ly-1]:                            #checking if two chars are same or not
        return 1 + LCS(x, y, lx-1, ly-1)
    else:                                               #third condition if above two are false
        return max(LCS(x , y ,lx ,ly-1) , LCS(x, y, lx-1,ly))




    
x=[]
with open('a_hash.txt', 'r') as f:#eventually read the file 1
    x = f.read().split()
x=pro_hash(x)



y=[]
with open('b_hash.txt', 'r') as f:#eventually read the file 2
    y = f.read().split()
y=pro_hash(y)



per=0
r=LCS(x,y,len(x),len(y))

if r==0:
    per=0
elif len(x)>len(y):
    per=r*100/len(x)
else:
    per=r*100/len(y)
print(per,"% files are same.")
