# 非递归实现
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]                                  #initialization
        out = []
        while stack:
            temp = stack.pop()                          
            out.append(temp.val)
            if temp.children:                           
                for item in temp.children[::-1]:
                    stack.append(item)
        return out

# 递归实现
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        s = bool(root) * [root]
        r = []
        
        while s:
            root = s.pop()
            r.append(root.val)
            s += root.children[::-1]
        
        return r
