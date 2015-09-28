from solver.cellgroups import CellGroup

class SubGroup(CellGroup):
    def __init__(self, box, index):
        super(SubGroup, self).__init__(box.sudoku)
        self.box = box
        self.index = index

    def get_box(self):
        return self.box

