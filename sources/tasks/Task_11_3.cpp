#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/helpers/Initializer.h"
#include "../../headers/tasks/Task_11_3.h"

void StartTask_11_3(int numberOfIterations, int n, double (*p) (int))
{
    double *brokenElements = new double[n + 1];
    InitArrayWithZeroes(brokenElements, n + 1);
    for (int i = 0; i < numberOfIterations; i++)
    {
        int count = 0;
        for (int j = 1; j <= n; j++)
            if (GetRandomDouble(0, 1) < p(j))
                count++;
        brokenElements[count]++;
    }
    double M = 0;
    double D = 0;
    for (int Xi = 0; Xi <= n; Xi++)
    {
        brokenElements[Xi] /= numberOfIterations;
        double XiPi = Xi * brokenElements[Xi];
        M += XiPi;
        D += XiPi * Xi;
    }
    D -= M * M;
    printf("Task 11.3:\nM = %.5f, D = %.5f\n", M, D);
}