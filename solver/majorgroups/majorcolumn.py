from majorgroup import MajorGroup

class MajorColumn(MajorGroup):
    def get_cells(self):
        cells = []
        for column in self.get_columns():
            cells += column
        return cells

    def get_column(self, index):
        return self.sudoku.get_column(self.index * 3 + index)

    def get_columns(self):
        return [self.sudoku.get_column(i) for i in range(index * 3, index * 3 + 3)]

    def get_boxes(self):
        return [self.sudoku.get_box(self.index, boxrow) for boxrow in range(0, 3)]

    def is_solved(self):
        if not super(MajorColumn, self).is_solved():
            return False

        for column in self.get_columns():
            if not column.is_solved():
                return False

        return True

    def __str__(self):
        return "MajorColumn<" + str(self.index) + ">"

