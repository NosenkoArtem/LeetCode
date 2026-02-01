from solution import Solution

solution = Solution()


def test_solution_1():
    assert sum(solution.sumZero(n = 5)) == 0


def test_solution_2():
    assert sum(solution.sumZero(n = 2)) == 0


def test_solution_3():
    assert sum(solution.sumZero(n = 1)) == 0