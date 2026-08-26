# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedvalue = -1001

        #pointers
        curr = head
        next = None

        while curr and curr.next:
            if curr.next.val == visitedvalue:
                return True
            curr.next.val = visitedvalue
            curr = curr.next
        return False