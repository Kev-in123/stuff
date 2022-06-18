#include <iostream>
#include <cmath>
#include <random>


int main() {
  // initialize variables for the number of points in and outside of a circle
  int in = 0;
  int total = 0;
  // seed
  srand(time(NULL));
  // loop 1,000,000 times, increase the value for more a more accurate result
  for (int i = 1; i < 1000000; i++) {
    // generate 1 point and calculates its distance from the origin
    float x = (float) rand() / RAND_MAX;
    float y = (float) rand() / RAND_MAX;
    double distance = pow(pow(x, 2) + pow(y, 2), 0.5);
    // check the distance and determine if it's in the circle
    if (distance <= 1) {
      in++;
    }
    total++;
  }
  // since the value of in/total is π/4, we multiply it by 4
  std::cout << (double) in / total * 4;
  std::cout << "\n";
}
