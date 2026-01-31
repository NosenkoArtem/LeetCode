from solution import Solution

solution = Solution()


def test_solution_1():
    assert solution.findClosest(x = 2, y = 7, z = 4) == 1


def test_solution_2():
    assert solution.findClosest(x = 2, y = 5, z = 6) == 2


def test_solution_3():
    assert solution.findClosest(x = 1, y = 5, z = 3) == 0