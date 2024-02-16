package leetcode;

/*
The task is to convert a string into a zigzag pattern with a specified number of rows.
The approach involves iterating through the string and placing characters in the appropriate rows based
on the zigzag pattern.
 */

/*
    Solution:

    1. Create an Array of StringBuffers:
    Create an array of StringBuffer to represent each row in the zigzag pattern.

    2. Iterate Through the String:
    Use a loop to iterate through each character in the string.
    Append characters to the rows in a zigzag pattern: vertically downward and then bent upward.

    3. Concatenate the Rows:
    Concatenate the rows to form the final zigzag pattern.

    4. Return the Result:
    Return the concatenated string as the result.

    Complexity
    Time complexity: O(N)
    Space complexity: O(N)
 */

public class LeetCode6ZigZagConversion {

    public String convert(String s, int numRows) {
        int n = s.length();
        StringBuffer[] arr = new StringBuffer[numRows];
        for (int i = 0; i < numRows; i++) {
            arr[i] = new StringBuffer();
        }

        int i = 0;
        while (i < n) {
            /// verticaly downword
            for (int ind = 0; ind < numRows && i < n; ind++) {
                arr[ind].append(s.charAt(i++));
            }
            /// bent upword
            for (int ind = numRows - 2; ind > 0 && i < n; ind--) {
                arr[ind].append(s.charAt(i++));
            }
        }
        StringBuffer ans = new StringBuffer();
        for (StringBuffer el : arr) {
            ans.append(el);
        }
        return ans.toString();
    }
}
