from tkinter import *
from tkinter import filedialog


class grid(Frame):
    '''object for a grid'''

    def __init__(self, master, width, height, numBombs):
        '''grid(master)
        creates a new blank grid'''
        # initialize a new Frame
        Frame.__init__(self,master,bg='black')
        self.grid()
        # put in lines between the cells
        # (odd numbered rows and columns in the grid)
        for n in range(1,2*height-1,2):
            self.rowconfigure(n,minsize=1)
        for n in range(1, 2*width-1, 2):
            self.columnconfigure(n,minsize=1)
        # thicker lines between 3x3 boxes and at the bottom
         # space at the bottom

        # create the cells
        self.cells = {} # set up dictionary for cells
        for row in range(height):
            for column in range(width):
                coord = (row,column)
                self.cells[coord] = cell(self,coord)
                # cells go in even-numbered rows/columns of the grid
                self.cells[coord].grid(row=2*row,column=2*column)

        self.scoreLabel = Label(self, text=str(numBombs), font=('Arial', 26))
        self.scoreLabel.grid(row=2*height, column= (int)(width) - 1, columnspan=2)


    def unhighlight_all(self):
        '''grid.unhighlight_all()
        unhighlight all the cells in the grid'''
        for cell in self.cells.values():
            cell.unhighlight()
class cell(Label):
    '''represents a cell'''

    def __init__(self,master,coord):
        '''cell(master,coord) -> cell
        creates a new blank cell with (row,column) coord'''
        Label.__init__(self,master,height=1,width=2,text='',\
                       bg='white',font=('Arial',24))
        self.coord = coord  # (row,column) coordinate tuple
        self.number = 0  # 0 represents an empty cell
        self.readOnly = False     # starts as changeable
        self.highlighted = False  # starts unhighlighted
        # set up listeners
        self.bind('<Button-1>',self.highlight)




    def is_highlighted(self):
        '''cell.is_highlighted() -> boolean
        returns True if the cell is highlighted, False if not'''
        return self.highlighted


    def highlight(self,event):
        '''cell.highlight(event)
        handler function for mouse click
        highlights the cell if it can be edited (non-read-only)'''
        if not self.readOnly:  # only act on non-read-only cells
            self.master.unhighlight_all()  # unhighlight any other cells
            self.focus_set()  # set the focus so we can capture key presses
            self.highlighted = True
            self['bg'] = 'lightgrey'

    def unhighlight(self):
        '''cell.unhighlight()
        unhighlights the cell (changes background to white)'''
        self.highlighted = False
        self['bg'] = 'white'

def play_minesweeper(width, height):
    root = Tk()
    root.title('Sudoku')
    sg = grid(root, width, height, 15)
    root.mainloop()

play_minesweeper(30, 15)
#class zeroMine:

#class numberMine:

#class