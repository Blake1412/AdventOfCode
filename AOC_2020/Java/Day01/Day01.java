import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day01 {
    ArrayList<Integer> data = new ArrayList<>();

    public Day01() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNext()) {
            data.add(scan.nextInt());
        }
        scan.close();
    }

    public int part1() {
        int answer = 0;
        for (int i = 0; i < data.size(); i++) {
            for (int j = i + 1; j < data.size(); j++) {
                if (data.get(i) + data.get(j) == 2020) {
                    answer = data.get(i) * data.get(j);
                }
            }
        }
        return answer;
    }

    public int part2() {
        int answer = 0;
        for (int i = 0; i < data.size(); i++) {
            for (int j = i + 1; j < data.size(); j++) {
                for (int k = j + 1; k < data.size(); k++) {
                    if (data.get(i) + data.get(j) + data.get(k) == 2020) {
                        answer = data.get(i) * data.get(j) * data.get(k);
                    }
                }
            }
        }
        return answer;
    }
}
