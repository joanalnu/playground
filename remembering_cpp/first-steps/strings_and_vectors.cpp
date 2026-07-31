#include <iostream>
#include <vector>  // Allows you to use dynamic arrays
#include <string>  // Allows you to use advanced text strings

int main() {
    // Creating a vector (dynamic array) of strings
    std::vector<std::string> tools = {"Clang++", "NeoVim", "Kitty", "Aerospace"};

    std::cout << "Your macOS C++ Setup Tools:" << std::endl;

    // Loop through the vector and print each string
    for (const std::string& tool : tools) {
        std::cout << "- " << tool << std::endl;
    }

    return 0;
}
