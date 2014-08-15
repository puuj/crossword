crossword
=========

Python library for handling crossword puzzles. This library provides a canonical data structure
that can be used to represent crosswords in your application. It provides a Pythonic way to
perform common operations on the grid, the words and the clues of the puzzle.

You can create a crossword:

    from crossword as Crossword

    puzzle = Crossword(15, 15)

You can iterate over rows and cells:

    for row in puzzle:
        for cell in row:
            pass

You also iterate using 'cells' (left-to-right, top-to-bottom):

    for x, y in puzzle.cells:
        print(x, y)

You can access a puzzle's metadata:

    creator = puzzle.meta.creator

You can also access all metadata attributes using dictionary syntax as meta is a dictionary:

    creator = puzzle.meta['creator']
    for key, value in puzzle.meta():
        print(key, value)

You can set a clue for an entry:

    puzzle.clues.across[1] = "This is a clue"
    puzzle.clues.down[2] = "This is a clue"

You can iterate over a crossword's clues (first Across, then Down):

    for direction, number, clue in puzzle.clues.all():
        print(direction, number, clue)

You can iterate over a crossword's clues in a particular direction:

    for number, clue in puzzle.clues.across():
        print(number, clue)
    for number, clue in puzzle.clues.down():
        print(number, clue)
