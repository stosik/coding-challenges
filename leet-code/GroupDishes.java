import java.util.AbstractMap;
import java.util.Arrays;
import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class GroupDishes {

  public static void main(String[] args) {
      String[][] dishes = new String[][] {
              {"Salad", "Tomato", "Cucumber", "Salad", "Sauce"},
              {"Pizza", "Tomato", "Sausage", "Sauce", "Dough"},
              {"Quesadilla", "Chicken", "Cheese", "Sauce"},
              {"Sandwich", "Salad", "Bread", "Tomato", "Cheese"}
      };

      String[][] result = Arrays.stream(dishes)
              .flatMap(d -> Arrays.stream(d)
                .skip(1)
                .map(i -> new AbstractMap.SimpleEntry(i, d[0])))
                .collect(Collectors.groupingBy(
                      Map.Entry::getKey, TreeMap::new, Collectors.mapping(Map.Entry::getValue, Collectors.toList())))
              .entrySet()
              .stream()
              .filter(e -> e.getValue().size() > 1)
              .map(e -> Stream.concat(Stream.of(e.getKey()), e.getValue().stream().sorted()).toArray(String[]::new))
              .toArray(String[][]::new);

      System.out.println(result[0][0]);
  }
}