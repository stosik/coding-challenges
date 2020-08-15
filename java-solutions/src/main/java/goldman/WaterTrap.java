package goldman;

public class WaterTrap {

    static int calculateWaterTrapped(int[] array) {
        int leftMax = 0;
        int rightMax = 0;
        int leftPointer = 0;
        int rightPointer = array.length - 1;

        int volume = 0;

        while (leftPointer + 1 < rightPointer) {
            leftMax = Math.max(leftMax, array[leftPointer]);
            rightMax = Math.max(rightMax, array[rightPointer]);

            int currentLevel = Math.min(leftMax, rightMax);
            if (leftMax < rightMax) {
                currentLevel -= array[leftPointer + 1];
                leftPointer++;
            } else {
                currentLevel -= array[rightPointer - 1];
                rightPointer--;
            }

            if (currentLevel > 0) {
                volume += currentLevel;
            }
        }

        return volume;
    }

    public static void main(String[] args) {
        //int[] array = new int[] {2, 1, 2}; // 1
        //int result_first = calculateWaterTrapped(array);
        //System.out.println(result_first);

        int[] array_two = new int[] {3, 0, 1, 3, 0, 5}; // 8
        int result_second = calculateWaterTrapped(array_two);
        System.out.println(result_second);
    }
}
