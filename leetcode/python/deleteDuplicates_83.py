# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3



# class ListNode:
#     def __init__(self, val = 0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(head):
        if (head == None) or (head.next == None):
            return head
        
        curr = head
        nxt = head.next 

        while(nxt != None):
            if curr.val == nxt.val:
                curr.next = nxt.next
                nxt = curr.next
            else:
                curr = curr.next
                nxt = nxt.next
        return head

        
