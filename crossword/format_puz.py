from puz import Puzzle

from crossword.compat import range
from crossword.core import Crossword


def from_puz(puzzle):
    result = Crossword(puzzle.width, puzzle.height)
    result.meta.creator = puzzle.author
    result.meta.rights = puzzle.copyright
    result.meta.title = puzzle.title
    rows = []
    for i in range(0, len(puzzle.solution), puzzle.width):
        if not puzzle.is_solution_locked():
            rows.append(puzzle.solution[i:i + puzzle.width])
        else:
            rows.append([None] * puzzle.width)
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            result[x, y].cell = cell
    result.block = '.'
    return result


def to_puz(crossword):
    pass
