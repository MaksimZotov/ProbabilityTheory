#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_5_27.h"

using namespace std;

void Task_5_27::Start(int numberOfIterations, double p1, double p2) {
    int count = 0;
    for (int i = 0; i < numberOfIterations; i++) {
        while (true) {
            if (getRandomDouble(0, 1) <= p1) {
                count++;
                break;
            }
            if (getRandomDouble(0, 1) <= p2)
                break;
        }
    }
    cout << "\nResult: " << (double)count / numberOfIterations << endl;
}
