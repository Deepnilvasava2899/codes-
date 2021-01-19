pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1


list=[12,45,6,78,91,30,57,79,68,79,6]
n=6
if search(list,n):
    print("found ",pos+1)
else:
    print("not found")
