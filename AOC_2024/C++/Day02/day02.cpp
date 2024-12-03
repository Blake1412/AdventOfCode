#include <fstream>
#include <iostream>
#include <span>
#include <sstream>
#include <string>
#include <vector>

#include "utils.h"

using namespace std;

vector<vector<int> > reports;

bool is_safe(const vector<int> &report)
{
    bool increasing = false;
    bool decreasing = false;
    for (int i = 0; i < report.size() - 1; i++)
    {
        int diff = report[i + 1] - report[i];
        if (abs(diff) < 1 or abs(diff) > 3) return false;

        if (diff > 0) increasing = true;
        else decreasing = true;

        if (increasing and decreasing) return false;
    }
    return true;
}

long long part1()
{
    long long safe = 0;
    for (const auto &report: reports)
    {
        if (is_safe(report)) safe++;
    }
    return safe;
}

long long part2()
{
    long long safe = 0;
    for (auto &report: reports)
    {
        if (is_safe(report))
        {
            safe++;
            continue;
        }

        for (int i = 1; i <= report.size(); i++)
        {
            vector<int> sub_report;
            sub_report.reserve(report.size() - 1);
            sub_report.insert(sub_report.begin(), report.begin(), report.begin() + i - 1);
            sub_report.insert(sub_report.end(), report.begin() + i, report.end());

            if (is_safe(sub_report))
            {
                safe++;
                break;
            }
        }
    }
    return safe;
}

int main()
{
    string line;
    ifstream file("../AOC_2024/C++/Day02/data.txt");

    while (getline(file, line))
    {
        vector<int> report;
        stringstream ss(line);
        int number;
        while (ss >> number)
        {
            report.push_back(number);
        }
        reports.push_back(move(report));
    }

    utils::timer(part1, part2);
}
