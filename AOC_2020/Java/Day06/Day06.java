import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day06 {
    List<List<String>> groups = new ArrayList<>();

    public Day06() throws FileNotFoundException {
        List<String> all = new ArrayList<>(Arrays.asList(new Scanner(new File("data.txt")).useDelimiter("\\Z").next().split("\r\n\r\n")));
        for (String group : all) {
            groups.add(Arrays.asList(group.split("\r\n")));
        }
    }

    public Set<Character> yesQuestions(List<String> group) {
        Set<Character> questions = new HashSet<>();
        for (String person : group) {
            for (int i = 0; i < person.length(); i++) {
                questions.add(person.charAt(i));
            }
        }
        return questions;
    }

    public int part1() {
        int sum = 0;
        for (List<String> group : groups) {
            sum += yesQuestions(group).size();
        }
        return sum;
    }

    public int part2() {
        int sum = 0;
        for (List<String> group : groups) {
            List<Character> questions = new ArrayList<>();
            for (String person : group) {
                for (int i = 0; i < person.length(); i++) {
                    questions.add(person.charAt(i));
                }
            }
            for (char question : yesQuestions(group)) {
                if (Collections.frequency(questions, question) == group.size()) {
                    sum++;
                }
            }
        }
        return sum;
    }
}
