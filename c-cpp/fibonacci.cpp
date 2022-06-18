#include <iostream>

int fib(int n) {
  if (n == 2 || n == 1) { // if the number requested is the 1st or 2nd fibonacci number
    return 1;
  }
  int r1 = 1; // calculate the nth fibonacci number
  int r2 = 1;
  int r = 0;
  for (int i = 0; i < n - 2; ++i) {
    r = r1 + r2;
    r2 = r1;
    r1 = r;
  }
  return r;
}

int main() {
  int n;
  std::cin >> n; std::cout << fib(n);
}
