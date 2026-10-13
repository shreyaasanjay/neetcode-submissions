# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #general idea
        #basically go through the bottom and return true for if its a leaf (all leaves are 
        #automatically balanced and then we also add one to the height and then we compare at the root 
        #if the height of the (actually maybe return the height) to find if its balanced we compare the

        


        #write a nested recursive function 
        def dfs(root):
            if not root:
                return [True,0]
            
            leftsub = dfs(root.left)
            rightsub = dfs(root.right)
            balanced = False
            if abs(leftsub[1]-rightsub[1]) <=1 and leftsub[0] and rightsub[0]:
                balanced=True
            
            return [balanced, 1+ max(rightsub[1], leftsub[1])]
        
        return dfs(root)[0]
            
        


        