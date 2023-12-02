package main

import (
	"../../../Utils"
	"os"
	"strings"
	"unicode"
)

var data []string

var numbers = map[string]int{
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

func main() {
	file, err := os.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}

	data = strings.Split(string(file), "\n")
	for _, row := range data {
		strings.Replace(row, "\r", "", -1)
	}

	Utils.Timer(part1, part2)
}

func part1() int {
	sum := 0
	for _, row := range data {
		sum += getFirstAndLastDigit(row, false)
	}
	return sum
}

func part2() int {
	sum := 0
	for _, row := range data {
		sum += getFirstAndLastDigit(row, true)
	}
	return sum
}

func getFirstAndLastDigit(s string, includeStrings bool) int {
	first, last := 0, 0

	for i := 0; first == 0 && i < len(s); i++ {
		if unicode.IsDigit(rune(s[i])) {
			first = int(s[i] - '0')
		} else if includeStrings {
			for j := i + 1; j <= len(s); j++ {
				if unicode.IsDigit(rune(s[j-1])) {
					break
				}
				if number, ok := numbers[s[i:j]]; ok {
					first = number
				}
			}
		}
	}

	for i := len(s); last == 0 && i > 0; i-- {
		if unicode.IsDigit(rune(s[i-1])) {
			last = int(s[i-1] - '0')
		} else if includeStrings {
			for j := i - 1; j >= 0; j-- {
				if unicode.IsDigit(rune(s[j])) {
					break
				}
				if number, ok := numbers[s[j:i]]; ok {
					last = number
				}
			}
		}
	}

	return first*10 + last
}
