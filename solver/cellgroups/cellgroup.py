from abc import ABCMeta, abstractmethod

class CellGroup(object):

    __metaclass__ = ABCMeta

    def __init__(self, sudoku):
        self.sudoku = sudoku

    @abstractmethod
    def get_cells(self):
        pass

    def get_unsolved_cells(self):
        return [cell for cell in self if not cell.is_solved()]

    def get_unsolved_values(self):
        values = set()
        for cell in self.get_unsolved_cells():
            values.update(cell.candidates)
        return values

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

    def __getitem__(self, index):
        return self.get_cells()[index]

    def __iter__(self):
        for cell in self.get_cells():
            yield cell

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return str(self)

