# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        level = []
        q = collections.deque()
        
        

        q.append(root)

        while q:
            for i in range(len(q)):
                value = q.popleft()
                #print(q)

                if value:
                    level.append(value.val)
                    q.append(value.left)
                    q.append(value.right)
                
            if level:
                result.append(level[-1])
            level = []

        return result
