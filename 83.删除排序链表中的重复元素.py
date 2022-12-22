#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if head == None:return head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next

            cur = cur.next
        return head


    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     cur = head.next
    #     left = head
    #     cache = head.val
    #     while cur:
    #         if cache != cur.val:
    #             cache = cur.val
    #             left.next = cur
            
    #         cur = cur.next
    #     return head
# @lc code=end

