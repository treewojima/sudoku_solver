from .cell import Cell
from .cellgroups import Box, Column, Grid, Row
from .majorgroups import MajorColumn, MajorRow
import pickle

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
        for boxrow in range(0, 3):
            for boxcol in range(0, 3):
                boxes.append(self.get_box(boxcol, boxrow))
        return boxes

    def get_unsolved_values(self):
        raise NotImplementedError()

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

    def save(self, filename = "savestate"):
        f = open(filename, "wb")
        pickle.dump(self.internal_grid, f, 2)
        f.close()

    def load(self, filename = "savestate"):
        f = open(filename, "rb")
        self.internal_grid = pickle.load(f)
        f.close()

    def __str__(self):
        return "Sudoku!"

