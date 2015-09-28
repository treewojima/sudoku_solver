from cell import Cell
from cellgroups import Box, Column, Grid, Row
from majorgroups import MajorColumn, MajorRow

class Sudoku(Grid):
    def __init__(self):
        cell_factory = lambda col, row: Cell(self, col, row)
        super(Sudoku, self).__init__(self, 9, cell_factory)

    def get_column(self, index):
        return Column(self, index)

    def get_columns(self):
        return [Column(self, index) for index in range(0, 9)]

    def get_major_column(self, index):
        return MajorColumn(self, index)

    def get_major_columns(self):
        return [MajorColumn(self, index) for index in range(0, 3)]

    def get_row(self, index):
        return Row(self, index)

    def get_rows(self):
        return [Row(self, index) for index in range(0, 9)]

    def get_major_row(self, index):
        return MajorRow(self, index)

    def get_major_rows(self):
        return [MajorRow(self, index) for index in range(0, 3)]

    def get_box(self, boxcol, boxrow):
        return Box(self, boxcol, boxrow)

    def get_boxes(self):
        boxes = []
        for boxrow in xrange(0, 3):
            for boxcol in xrange(0, 3):
                boxes.append(self.get_box(boxcol, boxrow))
        return boxes

    def is_solved(self):
        for column in self.get_columns():
            if not column.is_solved():
                return False

        for row in self.get_rows():
            if not row.is_solved():
                return False

        for box in self.get_boxes():
            if not box.is_solved():
                return False

        return True

    def __str__(self):
        return "Sudoku!"

def from_file(filename):
    lines = []
    try:
        f = file(filename)
        lines = [line.strip() for line in f.readlines()]
        f.close()
    except IOError, e:
        raise ParseError(filename, "could not open file: " + str(e))

    if len(lines) != 9:
        raise ParseError(filename, "mismatched number of rows in grid")

    grid = Grid()

    for row in range(0, 9):
        line = lines[row]
        if len(line) != 9:
            raise ParseError(filename, "mismatched number of cells in row \"" + str(row) + "\"")

        for col in range(0, 9):
            value = line[col]
            if value == "-":
                # The default value of cells in the grid is already range(1, 10)
                continue

            try:
                grid.get_cell(col, row).set_value(int(value))
            except IndexError, e:
                print "col=" + str(col)
                print "row=" + str(row)
                print "line=" + line
                print "value=" + str(value)
                raise e

    return grid
        
