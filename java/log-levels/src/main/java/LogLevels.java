public class LogLevels {
    
    public static String message(String logLine) {
        String[] words = logLine.trim().split(" ");
        String message = "";

        for (String string : words) {
            if (!string.isBlank() && !string.contains(":")) {
               message += string + " ";
            }
         }
         
        return message.trim();
    }

    public static String logLevel(String logLine) {
        String[] words = logLine.trim().split(" ");
        String target = words[0];

        return target.substring(1, target.length()-2).toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
