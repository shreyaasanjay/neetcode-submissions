# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #create a new linked list (called lsum)
        #the reason we want to create a dummy pointer pointer is because we dont want to modify lsum (the way to add to a linked list is to do pointer.next = New node and pointer=pointer.next)
        lsum = ListNode()
        #this is important, linked lists are traversed with pointers so we need a pointer starting at the head
        pointer = lsum
        valsum = 0
        #initialize carry to zero
        carry = 0
        
        while l1 != None or l2 != None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            valsum = val1 + val2 + carry
            carry = 0
            print("valsum")
            print(valsum)

            if valsum > 9:
                print("carry")
                carry = valsum // 10
                valsum = valsum - carry * 10
                print(valsum)
                
            
            pointer.next = ListNode(valsum)
            pointer=pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            print("lsum")
            print(pointer.val)
            
        if carry>0:
          pointer.next = ListNode(carry)
          pointer=pointer.next 

        if lsum.val == 0:
            lsum = lsum.next 
        return lsum



        
        
        
        
