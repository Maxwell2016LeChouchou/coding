# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# 暴力穷解
# Definition for singly-linked list
# class LinkNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def isPalindrome(head):
#     stack = []
#     while head != None:
#         stack.append(head.val)
#         head = head.next
#     return stack == stack[::-1]




# # 快慢指针 解法 1
# class LinkNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def isPalindrome(self, head):
#         if not head or not head.next: #链表为空或只有一个元素
#             return True
#         slow = head
#         fast = head.next      # 创建快慢指针，寻找链表中点
#         while fast and fast.next:
#             fast = fast.next.next 
#             if fast:  # 当前快指针fast的位置为奇数位置
#                 slow = slow.next   # 慢指针保持指向左侧最后一个元素
#         # second 要指向右侧第一个元素（偶）或是中间的右侧第一个元素（奇）
#         if fast: # 链表有奇数个元素
#             second = slow.next
#         else: 
#             second = slow.next.next
        
#         slow.next = None
#         first = head 
#         pre = None
#         while first: # 翻转左侧链表
#             tmp = first.next
#             first.next = pre
#             pre = first
#             first = tmp
#         first = pre
#         while first and second:
#             if first.val != second.val:
#                 return False
#             first = first.next
#             second = second.next
#         return True


# 快慢指针 解法 2:
class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next: # 创建快慢指针
            slow = slow.next
            fast = fast.next.next
        
        slow = slow.next
        new_head = None
        while slow:  # 链表反转
            p = slow
            slow = slow.next
            p.next = new_head
            new_head = p
        
        while new_head: # 反转链表与正向链表判定
            if head.val != new_head.val:
                return False
            new_head = new_head.next
            head = head.next
        return True

p1 = LinkNode(1)
p2 = LinkNode(4)
p3 = LinkNode(3)
p4 = LinkNode(5)
p5 = LinkNode(1)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
print(Solution().isPalindrome(p1))









    
