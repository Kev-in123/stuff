#include <iostream>

#define string std::string

void TowerOfHanoi(int n, string fromRod, string toRod, string spareRod) {
  if (n == 1) {
    std::cout << "Move disk 1 from rod " + fromRod + " to rod " + toRod + "\n"; // display the step
  }
  else {
    TowerOfHanoi(n - 1, fromRod, spareRod, toRod); // move the disk
    std::cout << "Move disk " << n << " from rod " + fromRod + " to rod " + toRod + "\n"; // display the step
    TowerOfHanoi(n - 1, spareRod, toRod, fromRod); // move the disk
  }
}

int main() {
  TowerOfHanoi(5, "left", "right", "middle");
}
