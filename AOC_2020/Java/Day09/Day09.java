import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day09 {
    List<Long> numbers = new ArrayList<>();

    public Day09() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNext()) {
            numbers.add(scan.nextLong());
        }
    }

    public long part1() {
        long number = 0;
        for (int i = 25; i < numbers.size(); i++) {
            List<Long> previousNumbers = new ArrayList<>(numbers.subList(i - 25, i));
            int flag = 0;
            for (int j = 0; j < previousNumbers.size() - 1; j++) {
                for (int k = j + 1; k < previousNumbers.size(); k++) {
                    if (previousNumbers.get(j) + previousNumbers.get(k) == numbers.get(i)) {
                        flag++;
                        break;
                    }
                }
            }
            if (flag == 0) {
                number = numbers.get(i);
                break;
            }
        }
        return number;
    }

    public long part2() {
        long number = part1();
        long sum = 0, encryptionWeakness = 0;

        for (int i = 0; i < numbers.indexOf(number); i++) {
            for (int j = i + 1; j < numbers.indexOf(number); j++) {
                List<Long> contiguousNumbers = new ArrayList<>(numbers.subList(i, j + 1));
                sum = 0;
                long max = 0, min = contiguousNumbers.get(0);
                for (long k : contiguousNumbers) {
                    sum += k;
                    max = Math.max(max, k);
                    min = Math.min(min, k);
                    if (sum >= number) {
                        break;
                    }
                }
                if (sum >= number) {
                    if (sum == number) {
                        encryptionWeakness = max + min;
                    }
                    break;
                }
            }
            if (sum == number) {
                break;
            }
        }
        return encryptionWeakness;
    }
}
