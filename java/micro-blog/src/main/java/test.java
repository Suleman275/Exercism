import java.util.stream.Collector;
import java.util.stream.Collectors;

public class test {
   public static void main(String[] args) {
      String x = "💇";
      String y = x.codePoints().limit(5).mapToObj(c -> Character.toChars(c)).collect(Collectors.joining();
      System.out.println(y);
   }
}
