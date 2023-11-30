import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Day05 {
    ArrayList<Integer> seats = new ArrayList<>();

    public Day05() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNext()) {
            seats.add(Integer.parseInt(scan.nextLine().replaceAll("[FL]", "0").replaceAll("[BR]", "1"), 2));
        }
        Collections.sort(seats);
    }

    public int part1() {
        return seats.get(seats.size() - 1);
    }

    public int part2() {
        int seatID = 0;
        for (int i = part1(); i > seats.get(0); i--) {
            if (!seats.contains(i)) {
                seatID = i;
                break;
            }
        }
        return seatID;
    }
}
