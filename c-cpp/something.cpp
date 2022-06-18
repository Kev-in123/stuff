#include <iostream>
#include <algorithm>

void print(int n) {
  std::cout << n;
}

int main() {
  int i[5] = { 1, 2, 3, 4, 5 };
  std::for_each(i, i + 5, print);
  std::cout << "\n";
  std::cout << "\n";
  std::for_each(i, i + 5, [](int n) {std::cout << n;});
  std::cout << "\n";
  std::cout << "\n";
  int a = 10;
  std::cout << a;
  std::cout << "\n";
  auto e {
    [a]() mutable {
      std::cout << --a;
      std::cout << "\n";
    }
  };
  e();
  e();
  std::cout << a;
  std::cout << "\n";
  std::cout << "\n";
  int b = 10;
  std::cout << b;
  std::cout << "\n";
  auto f {
    [&b]() mutable {
      std::cout << --b;
      std::cout << "\n";
    }
  };
  f();
  f();
  std::cout << b;
}