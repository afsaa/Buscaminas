import numpy
import random

width = raw_input("Digite el largo de la pantalla: ")
height = raw_input("Digite el alto de la pantalla: ")
mines = raw_input("Digite el numero de minas: ")

class Board:
    def __init__ (self, width, height, mines):
        self.rows = int(width)
        self.cols = int(height)
        self.matriz = numpy.chararray((self.rows, self.cols))
        self.mines = int(mines)

    def makeBlankBoard(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matriz[i][j] = C.states[0]

    def printBoard(self):
        print self.matriz

    def plantMines(self):
        for x in range(0, self.mines):
            self.matriz[random.randint(0, self.rows)][random.randint(0, self.cols)] = '*'

class Cell:
    def __init__ (self):
        self.states = ['.', '-', '*', 'P']
        self.actualState = ' '

    def gameOver(self):
        if (C.actualState == '*'):
            return False #To break the loop and end the game

C = Cell()
B = Board(width, height, mines)
B.makeBlankBoard()
B.plantMines()
B.printBoard()