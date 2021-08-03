# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        queue = [root]
        depth = 0
        
        newQueue = []
        while(queue):
            for curNode in queue:
                if curNode.left != None:
                    newQueue.append(curNode.left)
                if curNode.right != None:
                    newQueue.append(curNode.right)
            depth += 1
            queue = newQueue
            newQueue = []
        return depth