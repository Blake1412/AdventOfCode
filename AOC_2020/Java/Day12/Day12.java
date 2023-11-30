import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day12 {
    List<Character> instructions = new ArrayList<>();
    List<Integer> magnitudes = new ArrayList<>();

    public Day12() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNext()) {
            String st = scan.nextLine();
            instructions.add(st.charAt(0));
            magnitudes.add(Integer.parseInt(st.substring(1, st.length())));
        }
    }

    public int part1() {
        int direction = 90, horizontalPos = 0, verticalPos = 0;

        for (int i = 0; i < instructions.size(); i++) {
            char instruction = instructions.get(i);
            int magnitude = magnitudes.get(i);

            switch (instruction) {
                case 'N' -> verticalPos += magnitude;
                case 'S' -> verticalPos -= magnitude;
                case 'E' -> horizontalPos += magnitude;
                case 'W' -> horizontalPos -= magnitude;
                case 'R' -> direction += magnitude;
                case 'L' -> direction -= magnitude;
                case 'F' -> {
                    switch (((direction / 90) % 4)) {
                        case 0 -> verticalPos += magnitude;
                        case 2, -2 -> verticalPos -= magnitude;
                        case 1, -3 -> horizontalPos += magnitude;
                        case 3, -1 -> horizontalPos -= magnitude;
                    }
                }
            }
        }
        return Math.abs(horizontalPos) + Math.abs(verticalPos);
    }

    public int part2() {
        int horizontalPos = 0, verticalPos = 0, waypointHorizontalPos = 10, waypointVerticalPos = 1;

        for (int i = 0; i < instructions.size(); i++) {
            char instruction = instructions.get(i);
            int magnitude = magnitudes.get(i);

            switch (instruction) {
                case 'N' -> waypointVerticalPos += magnitude;
                case 'S' -> waypointVerticalPos -= magnitude;
                case 'E' -> waypointHorizontalPos += magnitude;
                case 'W' -> waypointHorizontalPos -= magnitude;
                case 'R' -> {
                    int x = waypointHorizontalPos, y = waypointVerticalPos;
                    waypointHorizontalPos = (int) Math.round((x * Math.cos(magnitude * Math.PI / 180)) + (y * Math.sin(magnitude * Math.PI / 180)));
                    waypointVerticalPos = (int) Math.round(-(x * Math.sin(magnitude * Math.PI / 180)) + (y * Math.cos(magnitude * Math.PI / 180)));
                }
                case 'L' -> {
                    int x = waypointHorizontalPos, y = waypointVerticalPos;
                    waypointHorizontalPos = (int) Math.round((x * Math.cos(Math.toRadians(magnitude))) - (y * Math.sin(Math.toRadians(magnitude))));
                    waypointVerticalPos = (int) Math.round((x * Math.sin(Math.toRadians(magnitude))) + (y * Math.cos(Math.toRadians(magnitude))));
                }
                case 'F' -> {
                    verticalPos += magnitude * waypointVerticalPos;
                    horizontalPos += magnitude * waypointHorizontalPos;
                }
            }
        }
        return Math.abs(horizontalPos) + Math.abs(verticalPos);
    }
}
