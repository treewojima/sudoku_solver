from cellgroup import CellGroup

class Row(CellGroup):
    def __init__(self, sudoku, index):
        super(Row, self).__init__(sudoku)
        self.index = index 

    def get_cells(self):
        return [self.sudoku.get_cell(column, self.index) for column in range(0, 9)]

    def get_major_row(self):
        return self.sudoku.get_major_row(self.index / 3)

    def __str__(self):
        return "Row<" + str(self.index) + ">"

