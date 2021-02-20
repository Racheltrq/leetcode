# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(root, lst):
        if root.left is None and root.right is None:
            lst.append(root.val)
            return lst
        if root.left is None:
            lst.append(root.val)
            lst.append(None)
            lst = traverse(root.right, lst)
            return lst
        if root.right is None:
            lst.append(root.val)
            lst = traverse(root.left, lst)
            lst.append(None)
            return lst
        else:
            lst.append(root.val)
            lst = traverse(root.left, lst)
            lst = traverse(root.right, lst)
            return lst
        
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        lst1 = traverse(q, [])
        lst2 = traverse(p, [])
        print(lst1, lst2)
        if len(lst1) != len(lst2):
            return False
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False
        return True