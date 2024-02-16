package leetcode;

/*
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
(similar to C/C++'s atoi function).
 */

/*
    Solution
    This is a solution in Java that converts a string to a 32-bit signed integer.

    The approach involves iterating through the input string and extracting the sign and digits
    of the integer. The solution uses a while loop to iterate through the string and check for
    whitespace, sign, and digits. The solution also checks for overflow conditions and returns
    Integer.MAX_VALUE or Integer.MIN_VALUE if the result is out of the range of a 32-bit signed integer.

    The solution returns the final result after applying the sign and digits to the result variable.
 */
public class LeetCode8StringToIntegerAtoi {

    private static final String WHITESPACE = " ";

    public int myAtoi(String s) {
        if (s.equals("")) {
            return 0;
        }

        // helper variables
        int res = 0;
        int i = 0;
        int sign = 1;

        // get rid of whitespace
        while (i < s.length() && s.charAt(i) == ' ') {
            i++;
        }

        // check for sign
        if (i < s.length() && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            // change if negative, iterate
            if (s.charAt(i++) == '-') {
                sign = -1;
            }
        }

        // now iterate across digits if any
        // should only be in range 0-9
        while (i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
            // check if we will go over the max
            if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && s.charAt(i) - '0' > 7)) {
                if (sign == -1) {
                    return Integer.MIN_VALUE;
                }
                return Integer.MAX_VALUE;
            }

            // update res
            res = res * 10 + (s.charAt(i++) - '0');
        }
        return sign * res;
    }
}
