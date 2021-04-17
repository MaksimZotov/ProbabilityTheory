#include <iostream>
#include <cmath>
#include "../../headers/helpers/NumberGenerator.h"

void StartTask_19_11(int numberOfIterations, double a)
{
    double s = 0;
    for (int i = 0; i < numberOfIterations; i++)
    {
        double x[3];
        double y[3];
        for (int j = 0; j < 2; j++)
        {
            while (true) {
                x[j] = GetRandomDouble(0, a);
                y[j] = GetRandomDouble(-a, a);
                if (x[j] * x[j] + y[j] * y[j] < a * a)
                    break;
            }
        }
        x[2] = 0;
        y[2] = GetRandomInt(0, 1) == 0 ? a : -a;
        s += abs((x[1] - x[0]) * (y[2] - y[0]) - (x[2] - x[0]) * (y[1] - y[0])) / 2;
    }
    printf("Task 19.11:\na = %.10f\nResult = %.10f\n", a, s / numberOfIterations);
}