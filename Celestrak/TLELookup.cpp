#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <satellite_name>" << std::endl;
        return 1;
    }

    std::string satName = argv[1];
    std::string line;
    std::string satLine1;
    std::string satLine2;
    std::string satLine3;

    std::ifstream myfile("Celestrak.txt");
    if (myfile.is_open()) {
        while (std::getline(myfile, line)) {
            if (line.find(satName) != std::string::npos) {
                satLine1 = line;
                std::getline(myfile, line);
                satLine2 = line;
                std::getline(myfile, line);
                satLine3 = line;
                break;
            }
        }
        myfile.close();
    } else {
        std::cerr << "Unable to open file" << std::endl;
        return 1;
    }

    // Convert std::string to const char*
    const char* cSatLine1 = satLine1.c_str();
    const char* cSatLine2 = satLine2.c_str();
    const char* cSatLine3 = satLine3.c_str();

    std::cout << cSatLine1 << std::endl;
    std::cout << cSatLine2 << std::endl;
    std::cout << cSatLine3 << std::endl;

    return 0;
}