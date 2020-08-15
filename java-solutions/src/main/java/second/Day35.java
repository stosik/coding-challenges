package second;/*
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first, the Gs come second,
and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
*/

public class Day35 {
    // Time complexity O(n)
    // Space complexity O(1)
    // Three way partition method
    static char[] sort(char[] rgb) {
        int left = 0;
        int middle = 0;
        int right = rgb.length - 1;

        char t;

        while(middle <= right) {
            if (rgb[middle] == 'R') {
                t = rgb[middle];
                rgb[middle] = rgb[left];
                rgb[left] = t;
                ++left;
                ++middle;
            } else if (rgb[middle] == 'B') {
                t = rgb[middle];
                rgb[middle] = rgb[right];
                rgb[right] = t;
                --right;
            } else {
                ++middle;
            }
        }

        return rgb;
    }

    public static void main(String[] args) {
        char[] rgb = new char [] { 'G', 'B', 'R', 'R', 'B', 'R', 'G' };
        char[] sortedRGB = sort(rgb);

        System.out.println(sortedRGB);
    }
}
