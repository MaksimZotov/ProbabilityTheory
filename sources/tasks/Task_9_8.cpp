#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_9_8.h"

void StartTask_9_8(int numberOfIterations, int minN, int maxN)
{
    int count = 0;
    int countUneven = 0;

    for (int i = 0; i < numberOfIterations; i++)
    {
        int n = GetRandomInt(minN, maxN);
        for (int j = 0; j < n; j++)
            countUneven += GetRandomInt(0, 1) == 1 ? 1 : 0;
        if (countUneven % 2 == 1)
            count++;
    }

    std::cout << "Task 9.8:" << std::endl;
    std::cout << "Result: " << (double)count / numberOfIterations << std::endl;
}