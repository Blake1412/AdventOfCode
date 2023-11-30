import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day08 {
    List<String> instructions = new ArrayList<>();
    List<Integer> arguments = new ArrayList<>();

    public Day08() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNext()) {
            String st = scan.nextLine();
            instructions.add(st.split(" ")[0]);
            arguments.add(Integer.parseInt(st.split(" ")[1]));
        }
    }

    private Map<Boolean, Integer> accumulatorValue(List<String> instructions) {
        List<Integer> checkedInstructions = new ArrayList<>();
        Map<Boolean, Integer> accumulatorLoopCheck = new HashMap<>();
        int accumulator = 0;

        for (int i = 0; i < instructions.size(); i++) {
            if (checkedInstructions.contains(i)) {
                accumulatorLoopCheck.put(true, accumulator);
                return accumulatorLoopCheck;
            }
            checkedInstructions.add(i);
            if (instructions.get(i).equals("acc")) {
                accumulator += arguments.get(i);
            } else if (instructions.get(i).equals("jmp")) {
                i += (arguments.get(i) - 1);
            }
        }
        accumulatorLoopCheck.put(false, accumulator);
        return accumulatorLoopCheck;
    }

    public int part1() {
        return accumulatorValue(instructions).get(true);
    }

    public int part2() {
        int accumulator = 0;

        for (int i = 0; i < instructions.size(); i++) {
            List<String> modifiedInstructions = new ArrayList<>(instructions);

            if (modifiedInstructions.get(i).equals("jmp")) {
                modifiedInstructions.set(i, "nop");
            } else if (modifiedInstructions.get(i).equals("nop")) {
                modifiedInstructions.set(i, "jmp");
            } else {
                continue;
            }

            if (accumulatorValue(modifiedInstructions).containsKey(false)) {
                accumulator = accumulatorValue(modifiedInstructions).get(false);
            }
        }
        return accumulator;
    }
}
