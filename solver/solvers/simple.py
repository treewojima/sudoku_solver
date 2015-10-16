def simple(sudoku):
    altered = False
    for cell in sudoku:
        if cell.is_solved():
            other_cells = set(cell.get_row().get_unsolved_cells())
            other_cells.update(cell.get_column().get_unsolved_cells())
            other_cells.update(cell.get_box().get_unsolved_cells())
            other_cells.difference_update(set([cell]))

            for other_cell in other_cells:
                altered += other_cell.remove_candidates([cell.get_value()])

    return altered

