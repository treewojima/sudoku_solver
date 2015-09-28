from solver.cellgroups import CellGroup

class MajorGroup(CellGroup):
    def __init__(self, sudoku, index):
        super(MajorGroup, self).__init__(sudoku)
        self.index = index

    def get_boxes(self):
        raise NotImplementedError()

    def is_solved(self):
        for box in self.get_boxes():
            if not box.is_solved():
                return False

        return True

