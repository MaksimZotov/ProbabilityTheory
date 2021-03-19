#include <iostream>
#include "../../headers/tasks/Task_12_1.h"

void StartTask_12_1(double x, double dx, double (*densityFun) (double x), double (*distributionFun) (double x))
{
    printf("Task 12.1:\n"
           "x = %.10f\n"
           "densityFun(x) = %.10f\n"
           "(distributionFun(x + dx) - distributionFun(x)) / dx = %.10f\n"
           "dx = %.10f\n",
           x, densityFun(x), (distributionFun(x + dx) - distributionFun(x)) / dx, dx);
}
