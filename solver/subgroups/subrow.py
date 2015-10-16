from .subgroup import SubGroup

class SubRow(SubGroup):
    def get_cells(self):
        return [self.box.get_cell(col, self.index) for col in range(0, 3)]

    def get_row(self):
        return self[0].get_row()

    def __str__(self):
        s = "SubRow<Box<" + str(self.box.boxcol) + "," + str(self.box.boxrow) + ">,"
        s += str([str(cell) for cell in self])
        return s

