#include "median.h"
#include <list>

void Median::addNum(int n) {
	nums.push_back(n);
}

double Median::findMedian() {
    nums.sort();
    std::list<int>::iterator index = nums.begin();
    int length = nums.size();
    int middle = length / 2;
    std::advance(index, middle);
    int val = *index;
    if (length % 2 != 0) {
        return val;
    }
    std::advance(index, -1);
    int val2 = *index;
    return (double) (val + val2) / 2;
}
