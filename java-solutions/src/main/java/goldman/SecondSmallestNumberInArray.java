package goldman;

public class SecondSmallestNumberInArray {

    static int findSecondSmallestNumberInArray(int[] array) {
        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for (int value : array) {
            if (value < smallest) {
                smallest = value;
            }

            if (value > smallest && value < secondSmallest) {
                secondSmallest = value;
            }
        }

        return secondSmallest;
    }

    public static void main(String[] args) {
        int[] array = new int[] { 12, 13, 1, 10, 34, 1};
        System.out.println(findSecondSmallestNumberInArray(array));
    }

}
