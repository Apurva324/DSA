# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        temp = head
        before = None
        pos = 1

        if (head == None):
            return None
        if (left == right):
            return head

        while (temp != None): # means there are elements in the LL
            if (pos < left):
                before = temp
                temp = temp.next
                pos += 1
                continue

            # if this not the case means you have arrived at pos = left
            curr = temp
            prev = None
            times = right - left + 1
            while (times!= 0):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                times -= 1

            temp.next = curr
            if(before!= None):
                before.next = prev
                return head
            return prev





        