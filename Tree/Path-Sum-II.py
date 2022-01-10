# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        curRes = []
        if root is None:
            return []
        self.helper(root, targetSum, curRes, res)
        return res
        
    def helper(self, curNode, targetSum, curRes, res):
        if curNode:
            if not curNode.left and not curNode.right:
                if curNode.val + sum(curRes) == targetSum:
                    curRes.append(curNode.val)
                    res.append(curRes)
                return

            self.helper(curNode.left, targetSum, curRes+[curNode.val], res)
            self.helper(curNode.right, targetSum, curRes+[curNode.val], res)
            return
