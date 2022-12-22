#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start


class Solution:
    '''
    insert and order
    not good enough
    '''
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     nums1[m:] = nums2
    #     nums1 = nums1.sort()


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n != 0:
            cur = m+n-1

            while cur >= 0:
                if nums1[m-1] >= nums2[n-1]:
                    nums1[cur] = nums1[m-1]
                    m-=1
                else:
                    nums1[cur] = nums2[n-1]
                    n-=1

                cur-=1
            pass


# @lc code=end

