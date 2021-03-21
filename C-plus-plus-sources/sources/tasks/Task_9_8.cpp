#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_9_8.h"

void StartTask_9_8(int numberOfIterations, int minN, int maxN)
{
    int count = 0; // Количество итераций, при которых герб появился нечётное количество раз

    for (int i = 0; i < numberOfIterations; i++)
    {
        int n = GetRandomInt(minN, maxN);  // minN и maxN задаются пользователем - это просто для
                                           // демонстрации того, что для любого n вероятность 0.5
        int countEmblem = 0;               // Количество подбрасываний, когда выпал герб
        for (int j = 0; j < n; j++)
            countEmblem += GetRandomInt(0, 1);
        if (countEmblem % 2 == 1)
            count++;
    }

    std::cout << "Task 9.8:" << std::endl;
    std::cout << "Result: " << (double)count / numberOfIterations << std::endl;
}