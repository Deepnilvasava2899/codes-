fileone=open('a_hash.txt','r')#this is the first file and we have accesed it
fone=fileone.read()
fone_split=fone.split(sep=' ')

filetwo=open('b_hash.txt','r')#this is for the second file and we hae accesed and read ot 
ftwo=filetwo.read()
ftwo_split=ftwo.split(sep=' ')

def hash(s):        #this is the hash function which will process the ascii into hash
    m1=5
    ans=0
    pro_pow=1
    for c in s:
        ans = (ans + (ord(c)+ord(c)+ord(c)+ord(c)+ord(c)) * pro_pow) / m1
        #p_pow = (p_pow * p) % m1

    return ans

def lcs(X, Y, j, k):  #least common multiple
  
    if j == 0 or k == 0: #if compares if the strings are same or not
       return 0
    elif X[j-1] == Y[k-1]:      #checks the previous and abouve value 
       return 1 + lcs(X, Y, j-1, k-1)
    else: 
       return max(lcs(X, Y, j, k-1), lcs(X, Y, j-1, k)) 

ffone=open('hash_file.txt','w')   #here we are writing the generated hash into annew text file
d=[]                                #an array to store the values
for e in fone_split:                
    hone=str(int(hash(e)))  
    d.append(hone)
    ffone.write(hone+' ')

    fftwo=open('hash_file1.txt','w')#here we are writing the generated hash into new file of text file 2
v=[]                                #an array to store the values
for e in ftwo_split:
    htwo=str(int(hash(e)))
    v.append(htwo)
    fftwo.write(htwo+' ')
    
fileone.close()                     #f1 closes


ffone.close()                       #f2 closes


filetwo.close()                     #f3 closes

fftwo.close()

print(d)                                #the hash compnonets will be writen

print(v)                                #the hash componentd os file 2 will be writtn

value=lcs(d,v,len(d),len(v))

print(value)

#made by deepnil vasava 18cp014
p=0
if len(d)>len(v):
    p=value*100/len(d)

else:
    p=value*100/len(v)
print(p,'%')
