import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day10 {
    List<Integer> jolts = new ArrayList<>(List.of(0));
    Map<Integer, Long> memo = new HashMap<>();

    public Day10() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNext()) {
            jolts.add(scan.nextInt());
        }
        Collections.sort(jolts);
        jolts.add(jolts.get(jolts.size() - 1) + 3);
    }

    public int part1() {
        int oneJolt = 0, threeJolt = 0;
        for (int i = 1; i < jolts.size(); i++) {
            int difference = jolts.get(i) - jolts.get(i - 1);
            switch (difference) {
                case 1 -> oneJolt++;
                case 3 -> threeJolt++;
            }
        }
        return oneJolt * threeJolt;
    }

    private long combinations(int index) {
        long sum = 0;

        if (memo.containsKey(index)) {
            return memo.get(index);
        }

        if (index == jolts.size() - 1) {
            return 1;
        }

        for (int i = 1; i <= 3; i++) {
            if ((index + i < jolts.size()) && ((jolts.get(index + i) - jolts.get(index)) <= 3)) {
                sum += combinations(index + i);
            }
        }

        memo.put(index, sum);
        return sum;
    }

    public long part2() {
        return combinations(0);
    }
}
