import unittest

import crossword

import puz


class PUZUnitTest(unittest.TestCase):

    def test_read_puz_to_crossword(self):
        puz_object = puz.read('fixtures/chronicle_20140815.puz')
        puzzle = crossword.from_puz(puz_object)
        self.assertEqual(
            puzzle.meta.title,
            'Que Pasa? - August 15, 2014'
        )
        self.assertEqual(
            puzzle.meta.creator,
            'by Ian Livengood / Edited by Brad Wilber '
        )
        self.assertEqual(puzzle.block, '.')

    def test_read_puz_locked_puzzle(self):
        puz_object = puz.read('fixtures/nyt_locked.puz')
        puzzle = crossword.from_puz(puz_object)
        for x, y in puzzle.cells:
            self.assertEqual(puzzle[x, y].cell, None)
