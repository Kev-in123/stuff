#include <iostream>

#define string std::string

void TowerOfHanoi(int n, string fromRod, string toRod, string spareRod) {
    if (n == 1) {
        std::cout << "Move disk 1 from rod " + fromRod + " to rod " + toRod + "\n"; // move the last disk
    }
    else {
        TowerOfHanoi(n - 1, fromRod, spareRod, toRod); // call the function with a disk moved
        std::cout << "Move disk " << n << " from rod " + fromRod + " to rod " + toRod + "\n"; //move the disk
        TowerOfHanoi(n - 1, spareRod, toRod, fromRod); // call the function with a disk moved
    }
}

int main() {
    TowerOfHanoi(5, "left", "right", "middle");
}
