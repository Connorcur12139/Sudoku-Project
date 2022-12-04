"""
Project: Project 4, Sudoku
Names: Connor Curcio, Matt Hand, Brandt Barton
Date: 12/04/2022
Class: COP3502C, Fall 2022
"""


class Cell:
    def __init__(self, screen, value = 0, row = 1, column = 1, ):
        self.value = value
        self.row = row
        self.column = column
        self.screen = screen

    def set_cell_value(self, cell_value):
        self.value = cell_value

    def set_sketched_value(self, sketched_value):
        self.value = sketched_value

    def draw(self):
        print("This method still needs to be completed to draw the cell in the PyGame UI")


