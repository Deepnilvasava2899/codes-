global N
N = int(input())

def nqueen(board,row):
    #if row is grater than n than written True
    if(row>=N):
        return True
    for i in range(N):
        if(check(board,row,i)):
            board[row][i] = 1
            if (nqueen(board, row + 1)==True):
                return True
            board[row][i] = 0

    # placing other queens
    #if(nqueen(board,row+1)):  #mistake found this will only check first iteration
    #    return True
    #else:
    #   return False
    return False


def check(board,row,coloumn):
    # check coloumn
    for i in range(N):
        if(board[i][coloumn]==1):
            #print("Deepnil")
            return False


    # for the upper right diagonal , range(coloumn,N,1) or not?
    for i,j in zip(range(row,-1,-1),range(coloumn,N)):
        if(board[i][j]==1):
            return False

    #for the upper left diagonal
    for i,j in zip(range(row,-1,-1),range(coloumn,-1,-1)):
        if(board[i][j]==1):
            return False

    return True



def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end = ' ')
        print()


board=[]
for i in range(N):
    new=[]
    for j in range(N):
        new.append(0)
    board.append(new)
if(nqueen(board,0)):
    print("solution for "+str(N) + " queen problem is:" )
    print_board(board)
else:
    print("solution not found")
