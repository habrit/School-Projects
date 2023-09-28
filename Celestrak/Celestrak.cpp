#include <iostream>
#include <cstdlib>

int main() {
    const char* command = "curl 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle' > Celestrak.txt"; // Replace with the command you want to run
    int result = std::system(command);

    if (result == 0) {
        std::cout << "Command executed successfully." << std::endl;
    } else {
        std::cerr << "Command failed with exit code " << result << std::endl;
    }

    return 0;
}