# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return None
        while head.val == val:
            head = head.next
            if head is None:
                return None
        prev = head
        cur = head.next
        while cur != None:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                prev, cur = cur, cur.next
        return head.val


p1 = ListNode(1)
p2 = ListNode(4)
p3 = ListNode(3)
p4 = ListNode(5)
p5 = ListNode(1)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
print(Solution().removeElements(p1, 1))
print(Solution().removeElements(p2, 1))
print(Solution().removeElements(p3, 1))
print(Solution().removeElements(p4, 1))
print(Solution().removeElements(p5, 1))

