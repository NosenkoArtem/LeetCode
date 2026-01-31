from solution import Solution

solution = Solution()


def test_solution_1():
    assert solution.nextGreatestLetter(letters=["c","f","j"], target = "a") == "c"


def test_solution_2():
    assert solution.nextGreatestLetter(letters = ["c","f","j"], target = "c") == "f"


def test_solution_3():
    assert solution.nextGreatestLetter(letters = ["x","x","y","y"], target = "z") == "x"