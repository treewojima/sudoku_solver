from .cellgroup import CellGroup

class Grid(CellGroup):
    def __init__(self, sudoku, size, cell_factory):
        super(Grid, self).__init__(sudoku)
        self.size = size
        self.internal_grid = [[cell_factory(column, row) for column in range(0, size)] for row in range(0, size)]

    def get_cell(self, column, row):
        try:
            return self.internal_grid[row][column]
        except IndexError as e:
            print("col=", column)
            print("row=", row)
            print("size=", self.size)
            raise e

    def get_cells(self):
        cells = [] 
        for row in self.internal_grid:
            cells += row
        return cells

    def print_state(self):
        for row in self.internal_grid:
            rowstr = ""
            for cell in row:
                if cell.is_solved():
                    rowstr += str(cell.get_value())
                else:
                    rowstr += "-"

            print(rowstr)

