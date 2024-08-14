from solution import Solution

solution = Solution()


def test_solution_1():
    assert solution.isPalindrome(121) == True


def test_solution_2():
    assert solution.isPalindrome(-121) == False


def test_solution_3():
    assert solution.isPalindrome(10) == False
