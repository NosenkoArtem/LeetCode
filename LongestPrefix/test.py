from solution import Solution

solution = Solution()


def test_solution_1():
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == 'fl'


def test_solution_2():
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == ''

