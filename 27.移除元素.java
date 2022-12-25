import java.util.ArrayList;

/*
 * @lc app=leetcode.cn id=27 lang=java
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        int right;
        for(int i = 0;i<nums.length;i++){
            right = i;
            if(nums[right] != val){
                nums[left] = nums[right];
                left++;
            }

        }

        return left;
    }
}
// @lc code=end

