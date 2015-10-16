from solver import Sudoku
from solver.solvers import simple, last_man_standing as lms, elimination as elim

def main():
    sudoku = from_file("puzzles/incomplete_sudoku.txt")

#    solvers = [simple, lms, elim]
#    while not sudoku.is_solved():
#        for solver in solvers:
#            if

    #    raise Exception("ambiguous puzzle (" + str(passes) + " passes)")

def debug():
    return from_file("puzzles/incomplete_sudoku.txt")

class ParseError(RuntimeError):
    def __init__(self, filename, msg):
        super(ParseError, self).__init__(filename + ": " + msg)

def from_file(filename):
    lines = []
    try:
        f = open(filename)
        lines = [line.strip() for line in f.readlines()]
        f.close()
    except IOError as e:
        raise ParseError(filename, "could not open file: " + str(e)).with_traceback()

    if len(lines) != 9:
        raise ParseError(filename, "mismatched number of rows in grid").with_traceback()

    sudoku = Sudoku()

    for row in range(0, 9):
        line = lines[row]
        if len(line) != 9:
            raise ParseError(filename, "mismatched number of cells in row \"" + str(row) + "\"").with_traceback()

        for col in range(0, 9):
            value = line[col]
            if value == "-":
                # The default value of cells in the grid is already range(1, 10)
                continue

            try:
                sudoku.get_cell(col, row).set_value(int(value))
            except IndexError as e:
                print("col=", str(col))
                print("row=", str(row))
                print("line=", line)
                print("value=", str(value))
                raise e

    return sudoku

if __name__ == "__main__":
    exit(main())
        
