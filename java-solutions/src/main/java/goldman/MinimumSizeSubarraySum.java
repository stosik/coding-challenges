package goldman;

public class MinimumSizeSubarraySum {

    static int minimumSizeSubarraySum(int[] array, int k) {
        int result = Integer.MAX_VALUE;
        int leftPointer = 0;
        int sum = 0;

        for (int i = 0; i < array.length; i++) {
            sum += array[i];
            while (sum >= k) {
                result = Math.min(result, i + 1 - leftPointer);
                sum -= array[leftPointer++];
            }
        }

        return (result != Integer.MAX_VALUE) ? result : 0;
    }

    public static void main(String[] args) {
        int[] array = new int[] { 2,3,1,2,4,3 };
        int k = 7;
        System.out.println(minimumSizeSubarraySum(array, k));
    }
}
