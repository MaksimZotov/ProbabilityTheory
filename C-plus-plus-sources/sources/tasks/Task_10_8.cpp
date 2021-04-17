#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/helpers/Initializer.h"

void StartTask_10_8(int numberOfIterations, int n, double p)
{
    int *mUnused = new int[n];
    int *mUsed = new int[n + 1];
    InitArrayWithZeroes(mUnused, n);
    InitArrayWithZeroes(mUsed, n + 1);
    for (int i = 0; i < numberOfIterations; i++)
    {
        for (int m = 1; m <= n; m++) { // m = количество использованных заготовок
            if (m == n)
            {
                mUnused[0]++;          // если m = n, то количество неиспользованных равно 0
                mUsed[n]++;            // если m = n, то количество использованных равно n
            }
            else if (GetRandomDouble(0, 1) < p)
            {
                mUnused[n - m]++;      // если m-ная деталь годная, то количество неиспользованных равно n - m
                mUsed[m]++;            // если m-ная деталь годная, то количество использованных равно m
                break;
            }
        }
    }
    printf("Task 10.8\n\n");
    for (int m = 1; m <= n; m++)
    {
        printf("P_unused (X = %d)\t%.6f\n", m - 1, (double)mUnused[m - 1] / numberOfIterations);
        printf("P_used (X = %d)\t\t%.6f\n\n", m, (double)mUsed[m] / numberOfIterations);
    }
    delete[] mUnused;
    delete[] mUsed;
}