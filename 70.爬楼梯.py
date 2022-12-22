#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,2
        if n == 1:return a
        if n == 2: return b

        for i in range(3,n+1):
            result = a + b
            a = b
            b = result

        return b





# @lc code=end

