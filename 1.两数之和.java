import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();

        for (int i = 0; i< nums.length;i++){
            if (map.containsKey(nums[i])){
                
                result[0] = map.get(nums[i]);
                result[1] = i;
                return result;
            }else{
                map.put(target-nums[i], i);
            }

        }

        return nums;

    }
}
// @lc code=end

