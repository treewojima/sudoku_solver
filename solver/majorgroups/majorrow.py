from .majorgroup import MajorGroup

class MajorRow(MajorGroup):
    def get_cells(self):
        cells = []
        for row in self.get_rows():
            cells += row
        return cells

    def get_row(self, index):
        return self.sudoku.get_row(self.index * 3 + index)

    def get_rows(self):
        return [self.sudoku.get_row(i) for i in range(self.index * 3, self.index * 3+ 3)]

    def get_boxes(self):
        return [self.sudoku.get_box(boxcol, self.index) for boxcol in range(0, 3)]

    def is_solved(self):
        if not super(MajorRow, self).is_solved():
            return False

        for row in self.get_rows():
            if not row.is_solved():
                return False

        return True

    def __str__(self):
        return "MajorRow<" + str(self.index) + ">"

