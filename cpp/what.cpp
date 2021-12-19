#include <iostream>

int main()
{
    std::string e = "no.";
    std::string& ee = e; // refrence var
    std::string* eee = &e; // pointer var
    std::cout << e << "\n";
    std::cout << ee << "\n";
    std::cout << eee << "\n";
    e = "yes.";
    ee = "idk.";
    std::cout << e << "\n";
    std::cout << ee << "\n";
    std::cout << eee << "\n";
}
