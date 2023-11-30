import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day11 {
    String[][] seatsRaw;

    public Day11() throws FileNotFoundException {
        List<List<String>> temp = new ArrayList<>();

        Scanner scan = new Scanner(new File("data.txt"));
        while (scan.hasNext()) {
            List<String> seatRows = new ArrayList<>();
            for (char ch : scan.nextLine().toCharArray()) {
                if (ch == 'L') {
                    seatRows.add("seatOccupied");
                } else {
                    seatRows.add("floor");
                }
            }
            temp.add(seatRows);
        }

        seatsRaw = new String[temp.size()][temp.get(1).size()];
        for (int i = 0; i < seatsRaw.length; i++) {
            for (int j = 0; j < seatsRaw[0].length; j++) {
                seatsRaw[i][j] = temp.get(i).get(j);
            }
        }
    }

    private String[][] seatChangeBasic(String[][] seatingArea) {
        String[][] seatingAreaCopy = new String[seatingArea.length][seatingArea[0].length];
        for (int i = 0; i < seatingArea.length; i++) {
            System.arraycopy(seatingArea[i], 0, seatingAreaCopy[i], 0, seatingArea[0].length);
        }


        for (int row = 0; row < seatingArea.length; row++) {
            for (int seat = 0; seat < seatingArea[0].length; seat++) {
                int occupiedNeighbours = 0;
                for (int i = -1; i <= 1; i++) {
                    for (int j = -1; j <= 1; j++) {
                        if ((row + i < 0) || (seat + j < 0) || (row + i >= seatingArea.length) || (seat + j >= seatingArea[row].length) || (j == 0 && i == 0)) {
                            continue;
                        }
                        if (seatingArea[row + i][seat + j].equals("seatOccupied")) {
                            occupiedNeighbours++;
                        }
                        if (occupiedNeighbours >= 4) {
                            break;
                        }
                    }
                }
                if (occupiedNeighbours >= 4 && seatingArea[row][seat].equals("seatOccupied")) {
                    seatingAreaCopy[row][seat] = "seatEmpty";
                }
                if (occupiedNeighbours == 0 && seatingArea[row][seat].equals("seatEmpty")) {
                    seatingAreaCopy[row][seat] = "seatOccupied";
                }
            }
        }
        if (Arrays.deepEquals(seatingAreaCopy, seatingArea)) {
            return seatingAreaCopy;
        } else {
            return seatChangeBasic(seatingAreaCopy);
        }
    }

    private String[][] seatChangeAdvanced(String[][] seatingArea) {
        String[][] seatingAreaCopy = new String[seatingArea.length][seatingArea[0].length];
        for (int i = 0; i < seatingArea.length; i++) {
            System.arraycopy(seatingArea[i], 0, seatingAreaCopy[i], 0, seatingArea[0].length);
        }


        for (int row = 0; row < seatingArea.length; row++) {
            for (int seat = 0; seat < seatingArea[0].length; seat++) {
                int occupiedNeighbours = 0;
                for (int i = -1; i <= 1; i++) {
                    for (int j = -1; j <= 1; j++) {
                        if ((row + i < 0) || (seat + j < 0) || (row + i >= seatingArea.length) || (seat + j >= seatingArea[row].length) || (j == 0 && i == 0)) {
                            continue;
                        }
                        int initI = i;
                        int initJ = j;
                        while (seatingArea[row + i][seat + j].equals("floor")) {
                            i += initI;
                            j += initJ;
                            if ((row + i < 0) || (seat + j < 0) || (row + i >= seatingArea.length) || (seat + j >= seatingArea[row].length)) {
                                i = initI;
                                j = initJ;
                                break;
                            }
                        }
                        if (seatingArea[row + i][seat + j].equals("seatOccupied")) {
                            occupiedNeighbours++;
                        }
                        if (occupiedNeighbours >= 5) {
                            break;
                        }
                        i = initI;
                        j = initJ;
                    }
                }
                if (occupiedNeighbours >= 5 && seatingArea[row][seat].equals("seatOccupied")) {
                    seatingAreaCopy[row][seat] = "seatEmpty";
                }
                if (occupiedNeighbours == 0 && seatingArea[row][seat].equals("seatEmpty")) {
                    seatingAreaCopy[row][seat] = "seatOccupied";
                }
            }
        }
        if (Arrays.deepEquals(seatingAreaCopy, seatingArea)) {
            return seatingAreaCopy;
        } else {
            return seatChangeAdvanced(seatingAreaCopy);
        }
    }

    public int part1() {
        int occupied = 0;

        for (String[] row : seatChangeBasic(seatsRaw)) {
            for (String seat : row) {
                if (seat.equals("seatOccupied")) {
                    occupied++;
                }
            }
        }
        return occupied;
    }

    public int part2() {
        int occupied = 0;

        for (String[] row : seatChangeAdvanced(seatsRaw)) {
            for (String seat : row) {
                if (seat.equals("seatOccupied")) {
                    occupied++;
                }
            }
        }
        return occupied;
    }
}
