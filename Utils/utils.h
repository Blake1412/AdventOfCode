#ifndef UTILS_H
#define UTILS_H
#include <functional>

class utils
{
public:
    static void timer(const std::function<long long()> &part1, const std::function<long long()> &part2);
};


#endif