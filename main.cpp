#include <ctime>
#include <cstdlib>
#include "headers/tasks/Task_11_3.h"

int main() {
    srand(time(NULL));
    StartTask_11_3(1000000, 5,
                   [](int numberOfElement) -> double { return 0.2 + 0.1 * (numberOfElement - 1); }
    );
    return 0;
}