package goldman;

import java.util.HashMap;
import java.util.Map;

public class FirstUniqueCharacterInString {

    static int firstUniqueCharacterInString(String input) {
        if (input == null) {
            return -1;
        }

        if (input.length() == 1) {
            return 0;
        }
        Map<Character, Integer> counts = new HashMap<>();
        for(int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            counts.put(c, counts.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < input.length(); i++) {
            if(counts.get(input.charAt(i)) == 1) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String input = "ANNABELLE";
        System.out.println(firstUniqueCharacterInString(input));
    }
}
