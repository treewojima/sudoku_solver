from sudoku import Sudoku

class Samurai(object):
    def __init__(self):
        self.sudokus = [Sudoku() for i in range(0, 5)]

        box1 = sudokus[0].get_box(2, 2)
        box2 = sudokus[4].get_box(0, 0)
        for i in range(0, 9):
            pass
