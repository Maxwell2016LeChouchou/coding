class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    curr_l1 = l1
    curr_l2 = l2
    head = None
    if curr_l1.val > curr_l2.val:
        head = curr_l1
        curr_l1 = curr_l1.next
    else:
        head = curr_l2
        curr_l2 = curr_l2.next
    curr_merged = head

    while curr_l1 is not None and curr_l2 is not None:
        if curr_l1.val < curr_l2.val:
            curr_merged.next = curr_l1
            curr_merged = curr_l1
            curr_l1 = curr_l1.next
        else:
            curr_merged.next = curr_l2
            curr_merged = curr_l2
            curr_l2 = curr_l2.next
    if curr_l2 == None:
        curr_merged.next = curr_l1
    if curr_l1 == None:
        curr_merged.next = curr_l2
    return head

l1 = [1,2,4,6,7]
l2 = [2,3,5,8]

print(mergeTwoLists(l1,l2)