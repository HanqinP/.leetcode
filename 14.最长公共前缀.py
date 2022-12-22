#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if len(strs) == 1:return prefix
        for i, char in enumerate(prefix):
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return prefix[:i]
        
        return prefix

# @lc code=end

