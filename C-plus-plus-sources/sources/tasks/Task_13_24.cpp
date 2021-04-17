#include <iostream>
#include <cmath>
#include "../../headers/tasks/Task_13_24.h"

void StartTask_13_24(double n)
{
    double h = 0.0001;
    double inf = 1000;
    double GFun = 0;
    for (double u = 0; u < inf; u += h)
        GFun += pow(u, n / 2 - 1) * exp(-u) * h;
    double M = 0;
    for (double x = 0; x < inf; x += h)
        M += x * (1 / (pow(2, n / 2) * GFun) * pow(x, n / 2 - 1) * exp(- x / 2)) * h;
    double D = 0;
    for (double x = 0; x < inf; x += h)
        D += pow(x - M, 2) * (1 / (pow(2, n / 2) * GFun) * pow(x, n / 2 - 1) * exp(- x / 2)) * h;
    printf("Task 13.24:\nn = %.10f\nM = %.10f\nD = %.10f\n", n, M, D);
}
