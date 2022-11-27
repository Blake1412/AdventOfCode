package Utils;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Utils {
    public static String readInput(int year, int day) {
        try {
            return new Scanner(new File(String.format("src\\_%d\\Day%02d\\input.txt", year, day))).useDelimiter("\\Z").next();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    public static String readTestInput(int year, int day) {
        try {
            return new Scanner(new File(String.format("src\\_%d\\Day%02d\\testInput.txt", year, day))).useDelimiter("\\Z").next();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}
