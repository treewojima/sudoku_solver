def last_man_standing(sudoku):
    altered = False

    for column in sudoku.get_columns():
        altered += work(column)

    for row in sudoku.get_rows():
        altered += work(row)

    for box in sudoku.get_boxes():
        altered += work(box)

    return altered

def work(cellgroup):
    altered = False

    for cell in cellgroup:
        if cell.is_solved():
            continue

        values = set()
        for other_cell in set(cellgroup).difference(set([cell])):
            values.update(other_cell.candidates)

        difference = cell.candidates.difference(values)
        if len(difference) == 1:
            cell.set_value(difference.pop())
            altered = True

    return altered
