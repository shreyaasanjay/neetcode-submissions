# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #brute force w array

        arrays = []

        #convert linked list into array

        curr = head
        while curr:
            arrays.append(curr.val)
            curr = curr.next
        print(arrays)

        #linked lists index work from the back and start at 1
        for i in range(len(arrays)+1):
            if i==n:
                arrays.pop(len(arrays)-n)
                print(arrays)
        
        curr=head

        if len(arrays)==0:
            head=None
        
        else:
            for i in range(len(arrays)):
                    curr.val = arrays[i]
                    prev=curr
                    curr = curr.next

            
            #remove the extra nodes at the end
            #start at head and then move on until 
            
            prev.next = None

        
        
        return head