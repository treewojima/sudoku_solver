class CellGroup(object):
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def get_cells(self):
        raise NotImplementedError()

    def is_solved(self):
        cell_values = []
        for cell in self:
            if not cell.is_solved():
                return False
            cell_values.append(cell.get_value())

        #if len(set(cell_values)) != 9:
        if len(cell_values) != len(set(cell_values)):
            return False

        return True

    def __iter__(self):
        for cell in self.get_cells():
            yield cell

    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        return str(self)

