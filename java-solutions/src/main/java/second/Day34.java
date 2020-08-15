package second;/*
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word.
If there is more than one palindrome of minimum length that can be made,
return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace",
since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
*/

import static java.lang.Integer.min;

public class Day34 {

    // Time complexity: O(n^2)
    // Space complexity: O(n^2)
    // Method: Dynamic programming (memoization)
    static int findMinimumInsertion(char[] str) {
        int n = str.length;
        if(n <= 1) {
            return 0;
        }

        int[][] table = new int[n][n];
        int l, h, gap;

        for(gap = 1; gap < n; gap++) {
            for(l = 0, h = gap; h < n; h++, l++) {
                table[l][h] = (str[l] == str[h])
                        ? table[l + 1][h - 1]
                        : min(table[l][h - 1], table[l + 1][h]) + 1;
            }
        }

        return table[0][n - 1];
    }

    public static void main(String[] args) {
        String str = "geeks";
        System.out.println(findMinimumInsertion(str.toCharArray()));
    }
}
