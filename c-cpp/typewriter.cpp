#include <iostream>

void typewriter(std::string n) {
    for (int i = 0; i < n.length(); ++i) { 
        std::cout << (n[i]); // print the character
    }
}
int main() {
	std::string n;
	std::cin >> n;
  typewriter(n);
}
