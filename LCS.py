def lcs(X,Y):               #two strings relatively x and y
    T= [[0 for i in range(10)]for j in range(10)]       #2d array
    for i in range(len(X)):             #loop 1
        for j in range(len(Y)):         #loop 2
            if(X[i]==Y[j]):                 #condition 1 if the string element match
                T[i][j]= 1+ T[i-1][j-1]     #here the 1 + diagonal element will be tken
            else:                           #condition 2 if both string are not same
                T[i][j]= max(T[i-1][j],T[i][j-1])   #take the max of the previous string and the above string
    return T[i][j]

X="deg"
Y="defg"
print(lcs(X,Y))
