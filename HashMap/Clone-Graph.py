"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        dict = {}
        
        def dfs(node):
            # Node already in the dictionary
            if node in dict:
                return dict[node]
            # Node not presented in the dictionary
            copy = Node(node.val)
            dict[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None