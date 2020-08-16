package goldman;

import java.util.HashMap;
import java.util.Map;

public class MostFrequentlyOccurringElementInArray {

    static int findMostOccurringElement(int[] array) {
        if (array.length == 0) {
            return -1;
        } else if (array.length == 1) {
            return array[0];
        }

        Map<Integer, Integer> counts = new HashMap<>();
        for(int i = 0; i < array.length; i++) {
            int number = array[i];
            counts.put(number, counts.getOrDefault(number, 0) + 1);
        }

        int maxCount = 0;
        int mostOccurring = -1;
        for(Map.Entry<Integer, Integer> element: counts.entrySet()) {
            if(maxCount < element.getValue()) {
                mostOccurring = element.getKey();
                maxCount = element.getValue();
            }
        }

        return mostOccurring;
    }

    public static void main(String[] args) {
        int[] array = new int[] { 1, 2, 3, 4, 5, 6, 6, 6, 1, 2 };
        System.out.println(findMostOccurringElement(array));
    }
}
