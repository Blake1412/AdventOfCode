#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>

#include "utils.h"

using namespace std;

vector<vector<int> > input_data = {{}, {}};

long long part1()
{
    long long sum = 0;
    for (int i = 0; i < input_data[0].size(); i++)
    {
        sum += abs(input_data[0][i] - input_data[1][i]);
    }
    return sum;
}

long long part2()
{
    long long sum = 0;
    unordered_map<int, int> frequencies;
    for (int i: input_data[0])
    {
        frequencies[i]++;
    }
    for (int i: input_data[1])
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
        input_data[0].push_back(left);
        input_data[1].push_back(right);
    }
    f.close();
    sort(input_data[0].begin(), input_data[0].end());
    sort(input_data[1].begin(), input_data[1].end());

    utils::timer(part1, part2);
}
