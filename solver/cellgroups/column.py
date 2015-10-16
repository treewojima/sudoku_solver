from .cellgroup import CellGroup

class Column(CellGroup):
    def __init__(self, sudoku, index):
        super(Column, self).__init__(sudoku)
        self.index = index

    def get_cells(self):
        return [self.sudoku.get_cell(self.index, row) for row in range(0, 9)]

    def get_major_column(self):
        return self.sudoku.get_major_column(self.index // 3)

    def __str__(self):
        return "Column<" + str(self.index) + ">"

