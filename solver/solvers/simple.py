def simple(sudoku):
    altered = False
    for cell in sudoku:
        if cell.is_solved():
            other_cells = set([c for c in cell.get_row() if not c.is_solved()])
            other_cells.update([c for c in cell.get_column() if not c.is_solved()])
            other_cells.update([c for c in cell.get_box() if not c.is_solved()])
            other_cells.difference_update(set([cell]))

            for other_cell in other_cells:
                altered += other_cell.remove_candidates([cell.get_value()])

    return altered

