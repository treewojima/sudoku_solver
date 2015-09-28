from grid import Grid

class Box(Grid):
    def __init__(self, sudoku, boxcol, boxrow):
        cell_factory = lambda col, row: sudoku.get_cell(boxcol * 3 + col, boxrow * 3 + row)

        super(Box, self).__init__(sudoku, 3, cell_factory)

        self.boxcol = boxcol
        self.boxrow = boxrow

    def __str__(self):
        return "Box<" + str(self.boxcol) + "," + str(self.boxrow) + "," + str([[str(self.get_cell(col, row)) for row in range(0, 3)] for col in range(0, 3)]) + ">"

