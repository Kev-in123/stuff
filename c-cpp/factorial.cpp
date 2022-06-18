#include <iostream>

void factorial(int n) {
  int fact = 1;
  for (int i = 1; i <= n; i++) {
    fact *= i;
  }
  std::cout << "The factorial of " << n << " is: " << fact;
}

int main() {
  factorial(5);
}
