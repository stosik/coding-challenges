package leetcode;

/*
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value
to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
 */

/*
    Solution
    This is a solution in Java that reverses an integer and checks if the result
    is within the range of a 32-bit signed integer.

    The approach involves using a while loop to extract the last digit of the input integer x
    and add it to a variable finalNum. At each iteration, finalNum is multiplied by 10 so that
    the next extracted digit can be added as the next significant digit. After the loop, finalNum is
    divided by 10 to remove the extra trailing zero.

    Next, the solution checks if finalNum is greater than the maximum value of a 32-bit signed
    integer (Integer.MAX_VALUE) or less than its minimum value (Integer.MIN_VALUE). If either of these
    conditions is met, the function returns 0 as the result will not fit within the range of a 32-bit signed integer.

    Finally, if x is negative, the solution returns -1 * finalNum as a negative result. If x is positive,
    the solution returns finalNum as the final answer.
 */
public class LeetCode7ReverseInteger {

    public int reverse(int x) {
        long finalNum = 0;
        while (x != 0) {
            int lastDig = x % 10;
            finalNum += lastDig;
            finalNum = finalNum * 10;
            x = x / 10;
        }
        finalNum = finalNum / 10;
        if (finalNum > Integer.MAX_VALUE || finalNum < Integer.MIN_VALUE) {
            return 0;
        }
        if (x < 0) {
            return (int) (-1 * finalNum);
        }
        return (int) finalNum;
    }
}
