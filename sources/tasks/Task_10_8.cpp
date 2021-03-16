#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/helpers/Initializer.h"
#include "../../headers/tasks/Task_10_8.h"

void StartTask_10_8(int numberOfIterations, int n, double p)
{
    int *mLeftover = new int[n];
    int *mUsed = new int[n + 1];
    InitArrayWithZeroes(mLeftover, n);
    InitArrayWithZeroes(mUsed, n + 1);
    for (int i = 0; i < numberOfIterations; i++) {
        for (int m = 1; m <= n; m++) {
            if (m == n) {
                mLeftover[n - m]++;
                mUsed[m]++;
            }
            else if (GetRandomDouble(0, 1) < p) {
                mLeftover[n - m]++;
                mUsed[m]++;
                break;
            }
        }
    }
    printf("Task 10.8\n\n");
    for (int m = 1; m <= n; m++) {
        printf("P_leftover (X = %d)\t%.6f\n", m - 1, (double)mLeftover[m - 1] / numberOfIterations);
        printf("P_used (X = %d)\t\t%.6f\n\n", m, (double)mUsed[m] / numberOfIterations);
    }
    delete[] mLeftover;
    delete[] mUsed;
}