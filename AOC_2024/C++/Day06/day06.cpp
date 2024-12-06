#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#include "utils.h"
using namespace std;

vector<vector<char> > map;
pair<int, int> start;
set<pair<int, int> > initial_seen;


bool is_loop()
{
    set<pair<pair<int, int>, pair<int, int> > > seen;
    pair dir = make_pair(-1, 0);
    pair cur_pos = start;

    while (true)
    {
        int x = cur_pos.first, y = cur_pos.second;
        int dx = cur_pos.first + dir.first, dy = cur_pos.second + dir.second;
        if (dx < 0 or dx >= map.size() or dy < 0 or dy >= map[0].size())
        {
            return false;
        }
        while (map[dx][dy] == '#')
        {
            const int temp = dir.first;
            dir.first = dir.second;
            dir.second = -temp;
            dx = x + dir.first, dy = y + dir.second;
            if (dx < 0 or dx >= map.size() or dy < 0 or dy >= map[0].size())
            {
                return false;
            }
        }
        if (seen.contains(make_pair(make_pair(dx, dy), dir)))
        {
            return true;
        }
        seen.insert(make_pair(make_pair(dx, dy), dir));
        cur_pos.first += dir.first;
        cur_pos.second += dir.second;
    }
}

long long part1()
{
    pair dir = {-1, 0};
    pair<int, int> cur_pos = start;
    while (true)
    {
        int x = cur_pos.first, y = cur_pos.second;
        int dx = x + dir.first, dy = y + dir.second;
        if (dx < 0 or dx >= map.size() or dy < 0 or dy >= map[0].size())
        {
            initial_seen.insert(cur_pos);

            break;
        }
        while (map[dx][dy] == '#')
        {
            const int temp = dir.first;
            dir.first = dir.second;
            dir.second = -temp;
            dx = x + dir.first, dy = y + dir.second;
        }
        initial_seen.insert(cur_pos);
        cur_pos.first += dir.first;
        cur_pos.second += dir.second;
    }
    return static_cast<long long>(initial_seen.size());
}

long long part2()
{
    long long total = 0;
    for (auto &row: map)
    {
        for (char &ch: row)
        {
            if (ch != '^' and ch != '#')
            {
                char temp = ch;
                ch = '#';
                total += is_loop();
                ch = temp;
            }
        }
    }
    return total;
}

int main()
{
    string line;
    ifstream file("../AOC_2024/C++/Day03/data.txt");

    while (getline(file, line))
    {
        stringstream ss(line);
        vector<char> row;
        char ch;
        while (ss >> ch)
        {
            row.push_back(ch);
        }
        map.push_back(row);
    }

    for (int i = 0; i < map.size(); i++)
    {
        for (int j = 0; j < map[i].size(); j++)
        {
            if (map[i][j] == '^')
            {
                start = make_pair(i, j);
            }
        }
    }

    utils::timer(part1, part2);
}
