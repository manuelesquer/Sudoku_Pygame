from random import shuffle
import copy

# Self algorithm that is going to complete row by row putting random numbers until get a combination lane that satisfy all the requirements
def solver(sudoku):
    numlist=[1,2,3,4,5,6,7,8,9]
    i=0
    while i<9:
        for j in range(9):
            shuffle(numlist) #shuffle the numbers to get a random sudoku
            for value in numlist: #loop the numbers until get one it fits correctly
                if not value in sudoku.table[i]: # check there is not a repeat value in the row
                    if not value in (sudoku.table[0][j],sudoku.table[1][j],sudoku.table[2][j],sudoku.table[3][j],sudoku.table[4][j],sudoku.table[5][j],sudoku.table[6][j],sudoku.table[7][j],sudoku.table[8][j]): #check there is not a repeat value in the col
                        square=[]
                        if i<3: #check there is not a repeat value in the square
                            if j<3:
                                square=[sudoku.table[r][0:3] for r in range(0,3)]
                            elif j<6:
                                square=[sudoku.table[r][3:6] for r in range(0,3)]
                            else:
                                square=[sudoku.table[r][6:9] for r in range(0,3)]
                        elif i<6:
                            if j<3:
                                square=[sudoku.table[r][0:3] for r in range(3,6)]
                            elif j<6:
                                square=[sudoku.table[r][3:6] for r in range(3,6)]
                            else:
                                square=[sudoku.table[r][6:9] for r in range(3,6)]
                        else:
                            if j<3:
                                square=[sudoku.table[r][0:3] for r in range(6,9)]
                            elif j<6:
                                square=[sudoku.table[r][3:6] for r in range(6,9)]
                            else:
                                square=[sudoku.table[r][6:9] for r in range(6,9)]

                        if not value in (square[0]+square[1]+square[2]):
                            sudoku.table[i][j]=value
            if sudoku.table[i][j]==0:
                sudoku.table[i]=[0,0,0,0,0,0,0,0,0]
                i-=1
                break

        i+=1
    return sudoku.table
