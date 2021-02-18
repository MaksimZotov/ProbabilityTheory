#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_9_8.h"

using namespace std;

void Task_9_8::Start(int numberOfIterations, int minN, int maxN)
{
    int count_uneven = 0;
    int count = 0;
    for (int i = 0; i < numberOfIterations; i++)
    {
        int n = getRandomInt(minN, maxN);
        for (int j = 0; j < n; j++)
            count_uneven += getRandomInt(0, 1) == 1 ? 1 : 0;
        if (count_uneven % 2 == 1)
            count++;
    }
    cout << (double)count / numberOfIterations << endl;
}