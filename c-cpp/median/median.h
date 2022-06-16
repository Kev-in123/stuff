#pragma once
#include <list>

class Median {
private:
  std::list<int> nums;
public:
  void addNum(int n);
  double findMedian();
};
