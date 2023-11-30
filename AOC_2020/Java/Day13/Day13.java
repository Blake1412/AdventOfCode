import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day13 {
    final int arrivalTime = 1003240;
    List<String> buses;
    List<Integer> busIDs = new ArrayList<>(), departurePositions = new ArrayList<>(), busIntervals;

    Day13() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("data.txt"));
        buses = new ArrayList<>(Arrays.asList(scan.nextLine().split(",")));

        int count = 0;
        for (String bus : buses) {
            if (!bus.equals("x")) {
                busIDs.add(Integer.parseInt(bus));
                departurePositions.add(count);
            }
            count++;
        }

        busIntervals = new ArrayList<>(buses.stream()
                .filter(x -> x.matches("\\d+"))
                .mapToInt(Integer::parseInt)
                .boxed()
                .toList());
    }

    public int part1() {
        int busArrivalTime = busIntervals.stream()
                .map(i -> (arrivalTime / i + 1) * i)
                .reduce(Integer::min)
                .orElseThrow();
        int busID = busIntervals.stream()
                .filter(x -> busArrivalTime % x == 0)
                .findFirst()
                .orElseThrow();

        return busID * (busArrivalTime - arrivalTime);
    }

    private boolean nextSyncedBus(long startPos, int syncedBuses) {
        if (startPos == 0) {
            return false;
        }
        return ((startPos + departurePositions.get(syncedBuses)) % busIDs.get(syncedBuses) == 0);
    }

    public Long part2() {
        long timestamp = busIDs.get(0), timestampInterval = busIDs.get(0);
        int syncedBuses = 1;

        while (syncedBuses < busIDs.size()) {
            while (!nextSyncedBus(timestamp, syncedBuses)) {
                timestamp += timestampInterval;
            }
            timestampInterval = timestampInterval * busIDs.get(syncedBuses);
            syncedBuses++;
        }
        return timestamp;
    }
}
