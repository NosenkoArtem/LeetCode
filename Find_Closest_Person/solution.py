class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dest_1, dest_2 = abs(z - x), abs(z - y)
        if dest_1 < dest_2:
            return 1
        elif dest_1 > dest_2:
            return 2
        else: 
            return 0