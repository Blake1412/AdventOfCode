import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day04 {

    ArrayList<HashMap<String, String>> passports = new ArrayList<>();
    ArrayList<String> fields = new ArrayList<>(Arrays.asList("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"));

    public Day04() throws FileNotFoundException {
        ArrayList<String> passportsUnsorted = new ArrayList<>(Arrays.asList(new Scanner(new File("data.txt")).useDelimiter("\\Z").next().split("\r\n\r\n")));
        for (String st : passportsUnsorted) {
            HashMap<String, String> passportFields = new HashMap<>();
            for (String fieldsUnsorted : st.split("\r\n")) {
                for (String keyValues : fieldsUnsorted.split(" ")) {
                    passportFields.put(keyValues.split(":")[0], keyValues.split(":")[1]);
                }
            }
            passports.add(passportFields);
        }
    }

    private boolean isValidPartOne(HashMap<String, String> passport) {
        for (String field : fields) {
            if (!passport.containsKey(field)) {
                return false;
            }
        }
        return true;
    }

    private boolean isValidPartTwo(HashMap<String, String> passport) {
        for (String field : fields) {
            String data = passport.get(field);
            switch (field) {
                case "byr" -> {
                    if (!(Integer.parseInt(data) >= 1920 && Integer.parseInt(data) <= 2002)) {
                        return false;
                    }
                }
                case "iyr" -> {
                    if (!(Integer.parseInt(data) >= 2010 && Integer.parseInt(data) <= 2020)) {
                        return false;
                    }
                }
                case "eyr" -> {
                    if (!(Integer.parseInt(data) >= 2020 && Integer.parseInt(data) <= 2030)) {
                        return false;
                    }
                }
                case "hgt" -> {
                    if (data.contains("cm")) {
                        int cm = Integer.parseInt(data.substring(0, data.indexOf("cm")));
                        if (!(cm >= 150 && cm <= 193)) {
                            return false;
                        }
                    } else if (data.contains("in")) {
                        int in = Integer.parseInt(data.substring(0, data.indexOf("in")));
                        if (!(in >= 59 && in <= 76)) {
                            return false;
                        }
                    } else {
                        return false;
                    }
                }
                case "hcl" -> {
                    Set<Character> characters = Set.of('a', 'b', 'c', 'd', 'e', 'f');
                    if (data.charAt(0) != '#') {
                        return false;
                    }
                    if (data.length() != 7) {
                        return false;
                    }
                    for (int i = 1; i < 7; i++) {
                        char ch = data.charAt(i);
                        if (!(Character.isDigit(ch) || characters.contains(ch))) {
                            return false;
                        }
                    }
                }
                case "ecl" -> {
                    Set<String> colors = Set.of("amb", "blu", "brn", "gry", "grn", "hzl", "oth");
                    if (!colors.contains(data)) {
                        return false;
                    }
                }
                case "pid" -> {
                    if (data.length() != 9) {
                        return false;
                    }
                    for (int i = 0; i < 9; i++) {
                        if (!(Character.isDigit(data.charAt(i)))) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }


    public int part1() {
        int valid = 0;
        for (HashMap<String, String> passport : passports) {
            if (isValidPartOne(passport)) {
                valid++;
            }
        }
        return valid;
    }

    public int part2() {
        int valid = 0;
        for (HashMap<String, String> passport : passports) {
            if (isValidPartOne(passport)) {
                if (isValidPartTwo(passport)) {
                    valid++;
                }
            }
        }
        return valid;
    }
}
