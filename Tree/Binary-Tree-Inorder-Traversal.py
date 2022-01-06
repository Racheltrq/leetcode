# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        elif root.left is None:
            res = [root.val]
            res.extend(self.inorderTraversal(root.right))
        elif root.right is None:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
        else:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res.extend(self.inorderTraversal(root.right))
        return res