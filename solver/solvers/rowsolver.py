from solver.majorgroups import MajorRow
from solver.subgroups import SubRow

def row_solver(sudoku):
    pass

def work(majorrow):
    altered = False

    for box in majorrow.get_boxes():
        altered += try_solve_box(box)

    return altered

def try_solve_box(box):
    majorrow = box.get_major_row()
    subrows = [SubRow(box, i) for i in range(0, 3)]
    other_boxes = set(majorrow.get_boxes()) - set([box])
    
    for subrow in subrows:
        for cell in subrow.get_unsolved_cells():
            
