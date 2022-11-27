package _2021.Day01;

import Utils.Utils;
import java.util.Arrays;

public class Day01 {

    static int[] depths;

    static {
        depths = Arrays.stream(Utils.readInput(2021, 1).split("\r\n")).mapToInt(Integer::parseInt).toArray();
    }

    public static int part1() {
        int count = 0;
        for (int i = 1; i < depths.length; i++) {
            if (depths[i] > depths[i - 1]) count++;
        }
        return count;
    }

    public static int part2() {
        int count = 0;
        for (int i = 3; i < depths.length; i++) {
            if (depths[i] + depths[i -1] + depths[i -2] > depths[i - 1] + depths[i - 2] + depths[i - 3]) count++;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(part1());
        System.out.println(part2());
    }
}
