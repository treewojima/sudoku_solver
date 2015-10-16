from abc import ABCMeta, abstractmethod
from solver.cellgroups import CellGroup

class MajorGroup(CellGroup):

    __metaclass__ = ABCMeta

    def __init__(self, sudoku, index):
        super(MajorGroup, self).__init__(sudoku)
        self.index = index

    @abstractmethod
    def get_boxes(self):
        pass

    def is_solved(self):
        for box in self.get_boxes():
            if not box.is_solved():
                return False

        return True

