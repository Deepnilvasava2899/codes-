#code by Ankur Patel on oct 6, 2020
#rat_maze backtracking

maze = [[1,1,0,0],
        [0,1,0,1],
        [1,1,1,0],
        [1,0,0,0],
        [1,1,1,1],]

#getting the number of rows and columns in maze M is number of row and N is number of column
global M,N
M = len(maze)
N = len(maze[0])

def rat_maze(maze,rat,row,column):
    if(move_d(maze,rat,row,column)):
        return True
    if (move_r(maze, rat, row, column)):
        return True
    #if solution not found
    return False




def move_d(maze,rat,row,column):
    if(row == M-1):
        return False
    if (row == M - 1 and column == N - 1):
        rat[row][column] = 1
        return True

    if(maze[row+1][column]==1):
        rat[row+1][column]=1
        if(move_l(maze,rat,row+1,column)):
            return True
        if(move_r(maze, rat, row + 1, column)):
            return True
        if (move_d(maze, rat, row + 1, column)):
            return True
        rat[row+1][column]=0
        return False


def move_l(maze,rat,row,column):
    if (column == 0):
        return False
    if (row == M - 1 and column == N - 1):
        rat[row][column] = 1
        return True

    if (maze[row][column-1] == 1):
        rat[row][column-1] = 1
        if (move_d(maze, rat, row, column-1)):
            return True
        if (move_u(maze, rat, row, column-1)):
            return True
        if (move_l(maze, rat, row, column-1)):
            return True
        rat[row][column-1] = 0
        return False

def move_r(maze,rat,row,column):
    if (column == N-1):
        return False
    if (row == M - 1 and column == N - 1):
        rat[row][column] = 1
        return True

    if (maze[row][column+1] == 1):
        rat[row][column+1] = 1
        if (move_d(maze, rat, row, column+1)):
            return True
        if (move_u(maze, rat, row, column + 1)):
            return True
        if (move_r(maze, rat, row, column + 1)):
            return True
        rat[row][column+1] = 0
        return False

def move_u(maze,rat,row,column):
    if (row == 0):
        return False
    if (row == M - 1 and column == N - 1):
        rat[row][column] = 1
        return True

    if (maze[row - 1][column] == 1):
        rat[row - 1][column] = 1
        if (move_r(maze, rat, row - 1, column)):
            return True
        if (move_l(maze, rat, row - 1, column)):
            return True
        if (move_u(maze, rat, row - 1, column)):
            return True
        rat[row + 1][column] = 0
        return False

#to print path of rat
def print_path(rat):
    for i in range(M):
        for j in range(N):
            print(rat[i][j],end = ' ')
        print()




rat = maze
#assigning all elements to 0, nice way found
rat = [[0 for j in  i] for i in rat ]
rat[0][0]=1

if(rat_maze(maze,rat,0,0)):
    print("path for rat is:")
    print_path(rat)
else:
    #print_path(rat)
    print("path not found.")

#print(maze,rat)
#print(M,N)
