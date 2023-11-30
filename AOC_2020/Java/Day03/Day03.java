import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day03 {
    ArrayList<ArrayList<Boolean>> treeRows = new ArrayList<>();

    public Day03() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNextLine()) {
            String st = scan.nextLine();
            ArrayList<Boolean> temp = new ArrayList<>();
            for (int i = 0; i < st.length(); i++) {
                if (st.charAt(i) == '#') {
                    temp.add(true);
                } else {
                    temp.add(false);
                }
            }
            treeRows.add(temp);
        }
        scan.close();
    }

    private int numberOfTrees(int slopeX, int slopeY) {
        int position = 0, answer = 0;

        for (int i = 0; i < treeRows.size(); i += slopeY) {
            if (treeRows.get(i).get(position)) {
                answer++;
            }
            position += slopeX;
            if (position > (treeRows.get(i).size() - 1)) {
                position -= treeRows.get(i).size();
            }
        }
        return answer;
    }

    public int part1() {
        return numberOfTrees(1, 2);
    }

    public long part2() {
        return (long) numberOfTrees(1, 1) *
                (long) numberOfTrees(3, 1) *
                (long) numberOfTrees(5, 1) *
                (long) numberOfTrees(7, 1) *
                (long) numberOfTrees(1, 2);
    }
}
