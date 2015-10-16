from .subgroup import SubGroup

class SubColumn(SubGroup):
    def get_cells(self):
        return [self.box.get_cell(self.index, row) for row in range(0, 3)]

    def get_column(self):
        return self[0].get_column()

    def __str__(self):
        s = "SubColumn<Box<" + str(self.box.boxcol) + "," + str(self.box.boxrow) + ">,"
        s += str([str(cell) for cell in self])
        return s

