#include <iostream>
#include <cmath>

bool isPrime(int n) {
    if (n < 2) { //check if the number is less than 2
        return false;
    }
    else if (n == 2) { //if the number is 2
        return true;
    } //if the number is prime and isn't 2 the check below should be true
    return (int) pow(2, n) % n == 2;
}
int main() {
	int n;
	std::cin >> n;
    std::cout << isPrime(n);
}
