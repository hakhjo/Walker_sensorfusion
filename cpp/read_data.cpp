#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <thread>

int main() {
    std::string line;
    const std::string file_path = "/workspace/data/input.txt";

    while (true) {
        std::ifstream data_file(file_path);

        if (data_file.is_open()) {
            std::cout << "Reading data from input.txt:" << std::endl;
            while (getline(data_file, line)) {
                std::cout << line << std::endl;
            }
            data_file.close();
        } else {
            std::cerr << "Unable to open file at " << file_path << std::endl;
        }

        // Wait a few seconds before the next read
        std::this_thread::sleep_for(std::chrono::seconds(5));
    }
    return 0;
}
