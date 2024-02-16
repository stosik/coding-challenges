package leetcode;

/*
Given an integer x, return true if x is a palindrome, and false otherwise.
*/

/*
    Solution
    This is a solution in Java that checks if an integer is a palindrome.

    The approach involves reversing the input integer and comparing it to the original integer.
    If the reversed integer is equal to the original integer, the function returns true. Otherwise, it returns false.

    To reverse the integer, the solution uses a while loop to extract the last digit of the input integer x
    and add it to a variable reversed. At each iteration, reversed is multiplied by 10 so that the next extracted digit
    can be added as the next significant digit. After the loop, the solution checks if the original integer is equal to the reversed integer and returns the result.
 */

public class LeetCode9PalindromeNumber {

    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int original = x;
        int reversed = 0;

        while (x != 0) {
            int digit = x % 10;
            System.out.println("digit: " + digit);
            reversed = reversed * 10 + digit;
            System.out.println("reversed: " + reversed);
            x /= 10;
        }

        return original == reversed;
    }
}

class Test {

    public static void main(String[] args) {
        LeetCode9PalindromeNumber leetCode9PalindromeNumber = new LeetCode9PalindromeNumber();
        System.out.println(leetCode9PalindromeNumber.isPalindrome(121));
        System.out.println(leetCode9PalindromeNumber.isPalindrome(-121));
    }
}