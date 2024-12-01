#include "utils.h"

#include <chrono>
#include <iomanip>
#include <iostream>


using namespace std;
using chrono::high_resolution_clock;
using chrono::duration;
using chrono::milliseconds;

void utils::timer(const function<long long()> &part1, const function<long long()> &part2)
{
    const auto t1 = high_resolution_clock::now();
    cout << "=====================================" << endl;
    cout << "Part 1" << endl;
    cout << "Answer: " << part1() << endl;
    cout << "Time: " << fixed << setprecision(3) << duration<double>(high_resolution_clock::now() - t1).count() << "s" << endl;
    const auto t2 = high_resolution_clock::now();
    cout << "=====================================" << endl;
    cout << "Part 2" << endl;
    cout << "Answer: " << part2() << endl;
    cout << "Time: " << duration<double>(high_resolution_clock::now() - t2).count() << "s" << endl;
    cout << "=====================================" << endl;
}
