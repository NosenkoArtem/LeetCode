from solution import Solution

solution = Solution()


def test_solution_1():
    assert solution.twoSum(nums=[2,7,11,15], target=9) == [0,1]


def test_solution_2():
    assert solution.twoSum(nums=[3,2,4], target=6) == [1,2]


def test_solution_3():
    assert solution.twoSum(nums=[3,3], target=6) == [0,1]