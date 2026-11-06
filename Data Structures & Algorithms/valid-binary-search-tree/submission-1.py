# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #so we're doing dfs because it doesnt make sense to check this laterally with bfs if we're doing each node and its children. So for the root (top value) the range is (-inf, +inf) and when we traverse, if we go left, then the max value decreases to that root value since it cannot be greater than the node about it. If we go right, the bottom values increases to the node above since it cannot be smaller than the parent node. If any node does not fall under this range we return False

        upper = math.inf
        lower = -1 * math.inf

        if root is None:
            return False

        def dfs(root, upper, lower):

            if root is None:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            else:
                return dfs(root.left, root.val, lower) and dfs(root.right, upper, root.val)
            
        
        return dfs(root, upper, lower)