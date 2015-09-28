class Cell(object):
    def __init__(self, sudoku, col, row):
        self.sudoku = sudoku
        self.col = col
        self.row = row
        self.candidates = set(range(1, 10))
    
    def set_value(self, n):
        if isinstance(n, set):
            if len(n) == 1:
                self.set_value(int(n.copy().pop()))
            else:
                validate_set(n)
                self.candidates = s

        elif isinstance(n, list):
            if len(n) == 1:
                self.set_value(int(n[0]))
            else:
                validate_list(n)
                self.candidates = set(n)

        elif isinstance(n, int):
            validate_num(n)
            self.candidates = set([n])
            
        else:
            raise TypeError("expecting argument of type 'set', 'list' or 'int'")    

    def get_value(self):
        # This exception is for debug purposes only
        if not self.is_solved():
            raise Exception("cell " + str(self) + " has multiple candidate values")

        return self.candidates.copy().pop()

    def remove_candidates(self, values):
        if isinstance(values, list):
            values = set(values)
        elif not isinstance(values, set):
            raise TypeError("expected argument of type 'set' or 'list'")

        new_candidates = self.candidates.difference(values)
        if self.candidates != new_candidates:
            self.candidates = new_candidates
            return True

        return False

    def get_column(self):
        return self.sudoku.get_column(self.col)

    def get_major_column(self):
        return self.get_column().get_major_column()

    def get_row(self):
        return self.sudoku.get_row(self.row)

    def get_major_row(self):
        return self.get_row().get_major_row()

    def get_box(self):
        boxcol = self.col / 3
        boxrow = self.row / 3
        return self.sudoku.get_box(boxcol, boxrow) 

    def is_solved(self):
        return (len(self.candidates) == 1)

    def __str__(self):
        return "Cell<" + str(self.col) + "," + str(self.row) + "," + str(self.candidates) + ">"

    def __repr__(self):
        return self.__str__()

def validate_set(s):
    for e in s:
        validate_num(e)

    return True

def validate_list(li):
    s = set(li)
    if len(li) != len(s):
        raise util.DuplicateValuesError()

    return validate_set(s)

def validate_num(n):
    if n < 1 or n > 9:
        raise util.RangeError(1, 9, n)
    return True

