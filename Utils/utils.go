package Utils

import (
	"fmt"
	"time"
)

func Timer(part1 func() int, part2 func() int) {
	fmt.Println("=====================================")
	now := time.Now().Nanosecond()
	fmt.Println("Part 1")
	fmt.Printf("Answer: %d\n", part1())
	fmt.Printf("%.3fs\n", float64(time.Now().Nanosecond()-now)/1e9)
	fmt.Println("=====================================")
	now = time.Now().Nanosecond()
	fmt.Println("Part 2")
	fmt.Printf("Answer: %d\n", part2())
	fmt.Printf("%.3fs\n", float64(time.Now().Nanosecond()-now)/1e9)
	fmt.Println("=====================================")
}
