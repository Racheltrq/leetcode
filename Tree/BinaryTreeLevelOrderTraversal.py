# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        queue = [root]
        res = [[root.val]]
        while len(queue) > 0:
            count = 0
            subres = []
            subresLen = len(queue)
            #print("queue length:", len(queue))
            while count < subresLen:
                curNode = queue.pop(0)
                #print("curNode:", curNode.val)
                if curNode.left != None:
                    queue.append(curNode.left)
                    subres.append(curNode.left.val)
                if curNode.right != None:
                    queue.append(curNode.right)
                    subres.append(curNode.right.val)
                count += 1
                #print("count:", count, "subres:", subres)
            if len(subres) > 0:
                res.append(subres)
                #print("res:", res)
        return res