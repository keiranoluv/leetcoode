# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if (head.next == None):
            return None
        
        node = head
        tmp = head

        i=1
        while (i<=n):
            node = node.next
            i+=1
        
        if (node == None):
            return head.next

        while(node.next !=None):
            node = node.next
            tmp = tmp.next

        # if (tmp.next!=None):
        tmp.next = tmp.next.next

        return head

"""
Ý tưởng: 
- cho node đi trước n bước để tạo chênh lệch với tmp
- Sau đó cho node và tmp cùng đi:
 => Nếu node gặp node cuối nghĩa là -> tmp cách end đúng n nodes.
"""