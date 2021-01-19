import random
import datetime


def generate(n):
    asc = []
    dsc = []
    random_num = []
    for i in range(0, n):
        asc.append(i)
    for i in range(n - 1, -1, -1):
        dsc.append(i)
    for i in range(0, n):
        random_num.append(random.randint(0, n))
    return asc, dsc, random_num


def bubblesort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                (array[i], array[j]) = (array[j], array[i])
    return array

def insertionsort(data):

    for i in range(1,len(data)):
        for j in range(i-1,0,-1):
            if  data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
            else:
                break
        return data


def selectionsort(data):
    for i in range(len(data)):
        index = i
        for j in range(i + 1, len(data)):
            if data[index] > data[j]:
                index = j
        data[i], data[index] = data[index], data[i]
    return data


## generate function returns 3 array
## ascending is at index 0 that is generate(size of array you want)[0]
## descending at 1 and random array at index 2

a = datetime.datetime.now()
print(bubblesort(generate(1000)[2]))
b = datetime.datetime.now()
print("time for bubblesort", b - a)

a = datetime.datetime.now()
print(insertionsort(generate(1000)[2]))
b = datetime.datetime.now()
print("time for insertionsort", b - a)

a = datetime.datetime.now()
print(selectionsort((generate(1000)[2])))
b = datetime.datetime.now()
print("time for selectionsort", b - a)

print("=============================================================")
print("for 10000")

a = datetime.datetime.now()
print(bubblesort(generate(10000)[2]))
b = datetime.datetime.now()
print("time for bubblesort", b - a)

a = datetime.datetime.now()
print(insertionsort(generate(10000)[2]))
b = datetime.datetime.now()
print("time for insertionsort", b - a)

a = datetime.datetime.now()
print(selectionsort((generate(10000)[2])))
b = datetime.datetime.now()
print("time for selectionsort", b - a)

print("=============================================================")
print("for 100000")

a = datetime.datetime.now()
print(bubblesort(generate(100000)[2]))
b = datetime.datetime.now()
print("time for bubblesort", b - a)

a = datetime.datetime.now()
print(insertionsort(generate(100000)[2]))
b = datetime.datetime.now()
print("time for insertionsort", b - a)

a = datetime.datetime.now()
print(selectionsort((generate(100000)[2])))
b = datetime.datetime.now()
print("time for selectionsort", b - a)
