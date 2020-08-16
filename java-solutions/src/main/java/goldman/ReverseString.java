package goldman;

public class ReverseString {

    static String withoutLibrary(String message) {
        char[] input = message.toCharArray();
        int begin = 0;
        int end = input.length - 1;

        while (end > begin) {
            char temp = input[begin];
            input[begin] = input[end];
            input[end] = temp;
            begin++;
            end--;
        }

        return new String(input);
    }

    static String withLibrary(String message) {
        return new StringBuilder(message).reverse().toString();
    }

    public static void main(String[] args) {
        String message = "reversed";
        System.out.println(withLibrary(message));
        System.out.println(withoutLibrary(message));
    }
}
