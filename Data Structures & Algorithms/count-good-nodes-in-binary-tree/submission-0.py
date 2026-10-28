# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        maxval = 0

        def dfs (root, maxval):

            if root==None:
                return 0

            if root.val>=maxval:
                res = 1
            else:
                res = 0
            maxval = max(root.val, maxval)
            
            res = res + dfs(root.right, maxval) + dfs(root.left, maxval)
            return res
        
        if root==None:
            return 0
        else:
            return dfs(root, root.val)





