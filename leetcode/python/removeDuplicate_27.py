# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3



# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicate(head):
    head = ListNode()
    if (head == None) or (head.next == None):
        return head
    
    cur = head
    nxt = head.next

    while(nxt != None):
        if cur.val == nxt.val:
            cur.next = nxt.next
            nxt = cur.next
        else:
            cur = cur.next
            nxt = nxt.next

    return head

head = [1,2,3,3,3,4,5,5,7]
print(deleteDuplicate(head))


