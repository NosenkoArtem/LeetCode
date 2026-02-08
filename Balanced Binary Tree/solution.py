# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_height(root) != -1
        
    def check_height(self, node: TreeNode):
        if not node:
            return 0
            
        # Рекурсивно проверяем левую сторону
        left_h = check_height(node.left)
        if left_h == -1: return -1
            
        # Рекурсивно проверяем правую сторону
        right_h = check_height(node.right)
        if right_h == -1: return -1
            
        # Если разница высот > 1, узел разбалансирован
        if abs(left_h - right_h) > 1:
            return -1
            
        # Возвращаем реальную высоту узла
        return max(left_h, right_h) + 1