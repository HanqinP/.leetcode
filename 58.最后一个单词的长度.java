/*
 * @lc app=leetcode.cn id=58 lang=java
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        String[] stringList = s.trim().split(" ");

        int len = stringList.length - 1;
        return len < 0 ? 0 : stringList[len].length();
    }
}
// @lc code=end
