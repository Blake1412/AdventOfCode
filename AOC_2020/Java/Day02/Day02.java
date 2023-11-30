import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day02 {
    ArrayList<String> frequencies = new ArrayList();
    ArrayList<Character> characters = new ArrayList();
    ArrayList<String> passwords = new ArrayList();


    public Day02() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNextLine()) {
            String st = scan.nextLine();
            frequencies.add(st.split(": ")[0].split(" ")[0]);
            characters.add(st.split(": ")[0].split(" ")[1].charAt(0));
            passwords.add(st.split(": ")[1]);
        }
        scan.close();
    }

    public int part1() {
        int answer = 0;

        for (int i = 0; i < passwords.size(); i++) {
            int count = 0;
            for (int j = 0; j < passwords.get(i).length(); j++) {
                if (passwords.get(i).charAt(j) == characters.get(i)) {
                    count++;
                }
            }
            if (count >= Integer.parseInt(frequencies.get(i).split("-")[0]) && count <= Integer.parseInt(frequencies.get(i).split("-")[1])) {
                answer++;
            }
        }
        return answer;
    }

    public int part2() {
        int answer = 0;

        for (int i = 0; i < passwords.size(); i++) {
            if (passwords.get(i).charAt(Integer.parseInt(frequencies.get(i).split("-")[0]) - 1) == characters.get(i) ^
                passwords.get(i).charAt(Integer.parseInt(frequencies.get(i).split("-")[1]) - 1) == characters.get(i)) {
                answer++;
            }
        }
        return answer;
    }
}
