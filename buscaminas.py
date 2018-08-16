
width = raw_input("Digite el largo de la pantalla: ")
height = raw_input("Digite el alto de la pantalla: ")
mines = raw_input("Digite el numero de minas: ")

class Board:
    def __init__ (self, width, height, mines):
        self.rows = int(width)
        self.cols = int(height) 
        #self.flag = flag
        self.mines = mines

    def makeBoard(self):
        pass
        
    def printBoard(self):
        print ('. '* self.rows + '\n')* self.cols

class Cell:
    def __init__ (self, x, y):
        self.posx = x
        self.posy = y
        self.state = ['.', '-', '*', 'P', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
x = 5
y = 6

C = Cell(x, y)
B = Board(width, height, mines)
B.printBoard()