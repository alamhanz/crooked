from typing import Optional


class ListNode:
    """_summary_"""

    def __init__(self, val=0, next=None):
        """_summary_

        Args:
            val (int, optional): _description_. Defaults to 0.
            next (_type_, optional): _description_. Defaults to None.
        """
        self.val = val
        self.next = next


class Solution:
    """_summary_"""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """_summary_

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        if head is not None:
            prev_node, curr_node = head, head.next
            prev_node.next = None

            while curr_node is not None:
                temp_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = temp_node

            return prev_node
        else:
            return None
