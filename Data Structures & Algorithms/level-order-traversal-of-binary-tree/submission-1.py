# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        #bfs with a queue - ig bfs is always done with queue

        #initialize the q with the top node only
        result = []
        q = collections.deque()
        q.append(root)

        print(q)
        #run this for the entire length of q
        while len(q)>0:
            qlength = len(q)
            level = []
            #for the length of q in the moment (at first its one node)
            for i in range(qlength):
                #pop each node and append to level 
                node = q.popleft()
                if node:
                    #if the node exists, we add all of those nodes to level, for each node you add their children
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)

        return result
        
        