## Run with[.../numbers_solver/tests/$]: nosetests --with-coverage --cover-package=.. __init__.py
import unittest

from hamcrest import assert_that, equal_to

from numbers_solver.src.numbers_backtracking import NumbersSolver


class testNumbers(unittest.TestCase):
    def setUp(self):
        self._numbers = NumbersSolver()

    def tearDown(self):
        del self._numbers

    def testTargetSolution(self):
        solution, _, _ = self._numbers.lookup(844, [100, 75, 50, 25, 10, 8])
        assert_that(solution[-1][-1], equal_to(844))

    def testTargetOptimalSolution(self):
        solution, _, _ = self._numbers.lookup(175, [100, 75, 50, 25, 10, 8])
        assert_that(len(solution), equal_to(1))

    def testApproxSolution(self):
        solution, _, _ = self._numbers.lookup(844, [3, 5, 4, 3, 2, 1])
        assert_that(solution[-1][-1], equal_to(540))
        assert_that(len(solution), equal_to(5))
