#include <iostream>
#include "median.h"

int main() {
  Median m;
  m.addNum(1);
  m.addNum(10);
  std::cout << m.findMedian();
}
