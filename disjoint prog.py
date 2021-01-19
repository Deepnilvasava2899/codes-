a=set([1,3,5,4,6,2])
b=set([7,8,9])
c=set([6,5,7,3])


print(a.isdisjoint(b))
print(a.isdisjoint(c))
print(b.isdisjoint(a))
print(b.isdisjoint(c))
print(c.isdisjoint(b))
print(a.isdisjoint(a))
