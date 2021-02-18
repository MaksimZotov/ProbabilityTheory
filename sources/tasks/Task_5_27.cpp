#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_5_27.h"

void StartTask_5_27(int numberOfIterations, double p1, double p2) {
    int count = 0;

    for (int i = 0; i < numberOfIterations; i++) {
        while (true) {
            if (GetRandomDouble(0, 1) <= p1) {
                count++;
                break;
            }
            if (GetRandomDouble(0, 1) <= p2)
                break;
        }
    }

    std::cout << "Task 5.27:" << std::endl;
    std::cout << "Result: " << (double)count / numberOfIterations << std::endl;
}
