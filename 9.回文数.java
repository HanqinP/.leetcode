/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if(x<0 || (x>0 && x%10==0)) return false;
        int result = 0;
        while (result < x){
            result = result*10 + x%10;
            x/=10;
        }


        return result == x || result/10 == x;
    }
}
// @lc code=end

