package _2021.Day02;

import Utils.Utils;

import java.util.Arrays;

public class Day02 {
    static String[][] instructions;

    static {
        instructions = Arrays.stream(Utils.readInput(2021, 2).split("\r\n"))
                             .map(s -> s.split(" "))
                             .toArray(String[][]::new);
    }

    public static int part1() {
        int horizontalPos = 0;
        int depth = 0;

        for (String[] instruction : instructions) {
            int magnitude = Integer.parseInt(instruction[1]);
            switch (instruction[0]) {
                case "forward" -> horizontalPos += magnitude;
                case "down" -> depth += magnitude;
                case "up" -> depth -= magnitude;
            }
        }
        return horizontalPos * depth;
    }

    public static int part2() {
        int horizontalPos = 0;
        int depth = 0;
        int aim = 0;

        for (String[] instruction : instructions) {
            int magnitude = Integer.parseInt(instruction[1]);
            switch (instruction[0]) {
                case "forward" -> {
                    horizontalPos += magnitude;
                    depth += aim * magnitude;
                }
                case "down" -> aim += magnitude;
                case "up" -> aim -= magnitude;
            }
        }
        return horizontalPos * depth;
    }

    public static void main(String[] args) {
        System.out.println(part1());
        System.out.println(part2());
    }
}
