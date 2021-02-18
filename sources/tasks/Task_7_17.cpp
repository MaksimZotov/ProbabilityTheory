#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_7_17.h"

using namespace std;

void Task_7_17::Start(int numberOfIterations, int numberOfButches, double percentOfSecondRate)
{
    int count1 = 0;
    int count2 = 0;
    int n = numberOfIterations;
    for (int i = 0; i < numberOfIterations; i++) {
        int butchWithSecondRate = getRandomInt(1, numberOfButches);
        int chosenButch = getRandomInt(1, numberOfButches);
        if (butchWithSecondRate == chosenButch) {
            if (getRandomDouble(0, 1) > percentOfSecondRate) {
                count1++;
                if (getRandomDouble(0, 1) > percentOfSecondRate)
                    count2++;
            }
            else
                n--;
        }
    }
    cout << (double)count1 / n << endl;
    cout << (double)count2 / n << endl;
}