class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    i = 0
    carry = 0
    result = ListNode(0)
    head = result 
    x, y = 0, 0
    while(l1 or l2):
        if (l1 != None):
            x = l1.val
            l1 = l1.next
        else:
            x = 0
        if (l2 !=None):
            y = l2.val
            l2 = l2.next
        else:
            y = 0
        sum = x + y + carry 
        result.next = ListNode(sum%10)
        result = result.next
        carry = sum//10
    if carry == 1:
        result.next = ListNode(1)
    return head.next

l1 = [3,4,2]
l2 = [4,6,5]

print(addTwoNumbers(l1,l2))