# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #this is example of dfs since you go all the way down for each done
        #when you need a global variable in recursion, you basically always need a helper function  because when u initialize to zero, it gets reset to zero every round 
        #had to look at solution agani


        #make this a global function variable
        self.diameter = 0
        
        if root==None:
            return 0
        

        def maxDepthperRoot(root):
            if root == None:
                return 0
            rightLength = maxDepthperRoot(root.right)
            leftLength = maxDepthperRoot(root.left)
            self.diameter = max(self.diameter, rightLength+leftLength)
            
            return 1+ max(rightLength, leftLength)
        
        maxDepthperRoot(root)
        return self.diameter
        
    
        