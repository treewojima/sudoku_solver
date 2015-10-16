from solver import Sudoku

class Samurai(object):
    def __init__(self):
        self.sudokus = [Sudoku() for i in range(0, 5)]

        box1 = self.sudokus[0].get_box(2, 2)
        box2 = self.sudokus[4].get_box(0, 0)
        merge_boxes(box1, box2)

        box1 = self.sudokus[1].get_box(0, 2)
        box2 = self.sudokus[4].get_box(2, 0)
        merge_boxes(box1, box2)

        box1 = self.sudokus[2].get_box(2, 0)
        box2 = self.sudokus[4].get_box(0, 2)
        merge_boxes(box1, box2)

        box1 = self.sudokus[3].get_box(2, 2)
        box2 = self.sudokus[4].get_box(0, 0)
        merge_boxes(box1, box2)

def merge_boxes(box1, box2):
    for i in range(0, 9):
        box2[i].candidates = box1[i].candidates

samurai = Samurai()
