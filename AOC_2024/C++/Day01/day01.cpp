#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>

#include "utils.h"

using namespace std;

vector<vector<int> > data = {{}, {}};

long long part1()
{
    long long sum = 0;
    for (int i = 0; i < data[0].size(); i++)
    {
        sum += abs(data[0][i] - data[1][i]);
    }
    return sum;
}

long long part2()
{
    long long sum = 0;
    unordered_map<int, int> frequencies;
    for (int i: data[0])
    {
        frequencies[i]++;
    }
    for (int i: data[1])
    {
        sum += i * frequencies[i];
    }
    return sum;
}

int main()
{
    string line;
    ifstream f("../AOC_2024/C++/Day01/data.txt");

    while (getline(f, line))
    {
        stringstream ss(line);
        int left, right;
        ss >> left >> right;
        data[0].push_back(left);
        data[1].push_back(right);
    }
    f.close();
    sort(data[0].begin(), data[0].end());
    sort(data[1].begin(), data[1].end());

    utils::timer(part1, part2);
}
