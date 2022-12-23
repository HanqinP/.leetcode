import java.util.HashMap;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {

        HashMap<Character,Character> map = new HashMap<Character,Character>();
        map.put('(',')');
        map.put('{','}');
        map.put('[',']');

        Stack<Character> stack = new Stack<Character>();

        for(int i=0;i<s.length();i++){
            if(map.containsKey(s.charAt(i))){
                stack.push(map.get(s.charAt(i)));
            }else{
                if(stack.empty()||stack.pop() != s.charAt(i)){
                    return false;
                }

            }
        }

        return stack.empty();
    }
}
// @lc code=end

