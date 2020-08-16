package goldman;

public class ValidPalindrome {

    static boolean isValidPalindrome(String word) {
        int leftPointer = 0;
        int rightPointer = word.length() - 1;

        while(leftPointer <= rightPointer) {
            if(word.charAt(leftPointer) != word.charAt(rightPointer)) {
                return false;
            }

            leftPointer++;
            rightPointer--;
        }

        return true;
    }

    public static void main(String[] args) {
        String word = "racecar";
        String wordTwo = "race";

        System.out.println(isValidPalindrome(word)); // true
        System.out.println(isValidPalindrome(wordTwo)); // false
    }
}
