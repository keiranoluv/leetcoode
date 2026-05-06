# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:



        if (head is None) or (head.next is None) or (k==0):
            return head

        size = 0
        cur = head
        while (cur):
            cur=cur.next
            size+=1
        k = k % size
        
        while (k>0):
            cur = head
            while(cur.next.next):
                cur = cur.next
            tmp = cur.next
            cur.next = None
            tmp.next = head
            head = tmp
            k-=1

        return head
        