package goldman;

public class StringCompression {

    static String compressString(String message) {
        if(message == null || message.length() == 1) {
            return message;
        }

        StringBuilder encodedMessage = new StringBuilder();

        for (int i = 0; i < message.length(); i++) {
            int count = 1;
            while (i < message.length() - 1 && message.charAt(i) == message.charAt(i + 1)) {
                i++;
                count++;
            }
            encodedMessage.append(message.charAt(i)).append(count);
        }

        return encodedMessage.toString();
    }

    public static void main(String[] args) {
        String word = "aaabbcdd";
        String compressedString = compressString(word);
        System.out.println(compressedString);
    }
}
