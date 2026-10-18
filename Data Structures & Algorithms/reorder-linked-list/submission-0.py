# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def recursive(root: ListNode, current: ListNode) -> ListNode:
            if not current:
                return root

            root = recursive(root, current.next)
            if not root:
                return None

            tmp = None
            if root == current or root.next == current:
                current.next = None
            else:
                tmp = root.next
                root.next = current
                current.next = tmp
        
            return tmp

        head = recursive(head, head.next)