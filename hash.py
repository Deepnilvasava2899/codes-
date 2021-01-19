def process_hash(x):
    ans=[]
    for i in x:
        m = 1000000009
        pr = 31
        pro_pow = 1
        hash_v = 0
        
        for j in i:
            hash_value=(hash_v + (ord(j)-ord('a')+1)*pro_pow)%m
            pro_pow = ( pro_pow * pr ) % m
        ans.append(hash_v)
    return ans



def LCS(x,y,d_x,d_y):
    if d_x==0 or d_y==0:                                  #this is the terminating condition
        return 0
    elif x[d_x -1] == y[d_y -1]:                            #this is used checking if two chars are same or not
        return 1 + LCS(x, y, d_x -1, d_y -1)
    else:                                               #third condition if above two are false
        return max(LCS(x , y ,d_x ,d_y -1) , LCS(x, y, d_x -1,d_y))
x=[]
with open('a.txt', 'r') as f:
    x = f.read().split()
x=process_hash(x)
y=[]
with open('b.txt', 'r') as f:
    y = f.read().split()
y=process_hash(y)
per=0
r=LCS(x,y,len(x),len(y))
if r==0:
    per=0
elif len(x)>len(y):
    per=r*100/len(x)
else:
    per=r*100/len(y)
print(per,"% files are same.")
