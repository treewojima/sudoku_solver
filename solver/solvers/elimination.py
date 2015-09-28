def elimination(sudoku):
    altered = False

    for column in sudoku.get_columns():
        altered += work(set(column))

    for row in sudoku.get_rows():
        altered += work(set(row))

    for box in sudoku.get_boxes():
        altered += work(set(box))

    return altered

def work(cellset):
    altered = False

    cell_matches = set()
    for c1 in cellset:
        for c2 in cellset - set([c1]):
            if c1.candidates.issuperset(c2.candidates) or c1.candidates == c2.candidates:
                cell_matches.update([c1, c2])
                
    candidates = set()
    for cell in cell_matches:
        candidates.update(cell.candidates)

    if len(candidates) == len(cell_matches):
        other_cells = cellset - cell_matches 
        for cell in other_cells:
            altered += cell.remove_candidates(candidates)

    return altered

