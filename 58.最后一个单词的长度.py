#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        if len(s) == 0:return 0
        if len(s) == 1:return len(s[0])

        return len(s[-1])

# @lc code=end

