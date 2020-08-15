package goldman;

public class FindRepeatingElementInArray {

    static void findRepeatingElement(int[] array) {
        for (int i = 0; i < array.length; i++) {
            if (array[Math.abs(array[i])] >= 0) {
                array[Math.abs(array[i])] = -array[Math.abs(array[i])];
            } else {
                System.out.println(Math.abs(array[i]));
            }
        }
    }

    public static void main(String[] args) {
        int [] array = new int [] { 1, 2, 3, 1, 3, 6, 6 };
        findRepeatingElement(array);
    }
}
