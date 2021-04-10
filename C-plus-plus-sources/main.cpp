#include <ctime>
#include <cstdlib>
#include "headers/tasks/Task_13_24.h"
#include "headers/tasks/Task_19_11.h"

int main() {
    srand(time(NULL));
    StartTask_13_24(4);
    StartTask_13_24(50);
    StartTask_13_24(128);
    StartTask_19_11(10000000, 5);
    StartTask_19_11(10000000, 10);
    return 0;
}


