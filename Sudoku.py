import pygame
from random import randint, shuffle
import numpy as np
from Cube import Cube
from Solver import *


class Sudoku:

    def __init__(self):

        self.table = []
        self.table.append([0,0,0,0,0,0,0,0,0])
        self.table.append([0,0,0,0,0,0,0,0,0])
        self.table.append([0,0,0,0,0,0,0,0,0])
        self.table.append([0,0,0,0,0,0,0,0,0])
        self.table.append([0,0,0,0,0,0,0,0,0])
        self.table.append([0,0,0,0,0,0,0,0,0])
        self.table.append([0,0,0,0,0,0,0,0,0])
        self.table.append([0,0,0,0,0,0,0,0,0])
        self.table.append([0,0,0,0,0,0,0,0,0])

        self.table_solution=[]

        self.rows = 9
        self.cols= 9
        self.width=540
        self.height=540
        self.cubes=[[Cube(self.table[i][j],i,j,self.width,self.height) for j in range(9)] for i in range(9)]
        self.selected=None



    def update_table(self):
        self.table = [[self.cubes[i][j].value for j in range(9)] for i in range(9)]

    # Check if the temporal number it is correct and place it
    def place(self,val):
        row, col = self.selected
        # We call function check if the number is correct or not
        if self.check(val, [row,col]):
            self.cubes[row][col].set(val)
            self.update_table()
            return True
        else:
            self.clear()
            self.update_table()
            return False

    # It save your temporal value that you inserted
    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    # Select the square that you clicked
    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    # Eliminate the temporal value of the square
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0: #If the square is empty it eliminates
            self.cubes[row][col].set_temp(0)

    # Get the position of the mouse when you click
    def click(self, pos):
            if pos[0] < self.width and pos[1] < self.height:
                gap = self.width / 9
                x = pos[0] // gap
                y = pos[1] // gap
                return (int(y),int(x))
            else:
                return None

    # Check if Sudoku is finished
    def check_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    # Check if the number is correct
    def check(self,nnum,pos):
        if self.table_solution[pos[0]][pos[1]]==nnum:
            return True
        return False

    # Create the solution of the Sudoku that is going to play
    def create_table(self):
        self.table=solver(self)
        self.table_solution=copy.deepcopy(self.table)

    # Eliminate random numbers to get ready the sudoku
    def eliminate_numbers(self):
        for j in range(3):
            for i in range(3):
                numlist=[3*i+1+27*j,3*i+1+27*j+1,3*i+1+27*j+2,3*i+1+27*j+9,3*i+1+27*j+10,3*i+1+27*j+11,3*i+1+27*j+18,3*i+1+27*j+20,3*i+1+27*j+21]
                shuffle(numlist)
                count =0
                for value in numlist:
                    value=value-1
                    self.table[(value//9)-1][(value%9)-1]= 0
                    count+=1
                    if count ==4:
                        break
        self.cubes=[[Cube(self.table[i][j],i,j,self.width,self.height) for j in range(9)] for i in range(9)]
