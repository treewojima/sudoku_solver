import solver

def main():
    sudoku = debug()

    passes = 1
    while not sudoku.is_solved():
        if simple_solver(sudoku):
            passes += 1
            continue
        
#        elif 

    #    raise Exception("ambiguous puzzle (" + str(passes) + " passes)")

def debug():
    return from_file("puzzles/incomplete_sudoku.txt")

class ParseError(RuntimeError):
    def __init__(self, filename, msg):
        super(ParseError, self).__init__(filename + ": " + msg)

def from_file(filename):
    lines = []
    try:
        f = file(filename)
        lines = [line.strip() for line in f.readlines()]
        f.close()
    except IOError, e:
        raise ParseError(filename, "could not open file: " + str(e))

    if len(lines) != 9:
        raise ParseError(filename, "mismatched number of rows in grid")

    sudoku = solver.Sudoku()

    for row in range(0, 9):
        line = lines[row]
        if len(line) != 9:
            raise ParseError(filename, "mismatched number of cells in row \"" + str(row) + "\"")

        for col in range(0, 9):
            value = line[col]
            if value == "-":
                # The default value of cells in the grid is already range(1, 10)
                continue

            try:
                sudoku.get_cell(col, row).set_value(int(value))
            except IndexError, e:
                print "col=" + str(col)
                print "row=" + str(row)
                print "line=" + line
                print "value=" + str(value)
                raise e

    return sudoku

if __name__ == "__main__":
    exit(main())
        
