#include <iostream>
#include <math.h>
#include "../../headers/tasks/Task_3_6.h"
#include "../../headers/helpers/NumberGenerator.h"

void GetRandomPointInsideOfEllipse(double ellA, double ellB, double* x, double* y) {
    while (true) {
        *x = GetRandomDouble(-ellA, ellA);
        *y = GetRandomDouble(-ellB, ellB);

        if (*x * *x / (ellA * ellA) + *y * *y / (ellB * ellB) <= 1)
            break;
    }
}

bool CheckIntersectionWithRectangle(double x, double y, double r, double recX, double recY)
{
    double absX = abs(x);
    double absY = abs(y);

    return absX > recX && absY > recY && sqrt(pow(absX - recX, 2) + pow(absY - recY, 2)) <= r ||
           absX < recX && absY - r <= recY || absY < recY && absX - r <= recX;
}

bool CheckNonIntersection(double x, double y, double r, double ellA, double ellB, double recX,
                          double recY, double circles[][2], int n, double stepX, double epsY)
{
    for (int i = 0; i < n; i++)
        if (sqrt(pow(x - circles[i][0], 2) + pow(y - circles[i][1], 2)) < 2 * r)
            return false;

    if (CheckIntersectionWithRectangle(x, y, r, recX, recY))
        return false;

    double absX = abs(x);
    double absY = abs(y);
    for (double xx = absX - r; xx < absX + r; xx += stepX)
        if (abs((absY + sqrt(pow(r, 2) - pow(xx - absX, 2))) - (ellB * sqrt(1 - pow(absX / ellA, 2)))) < epsY)
            return false;

    return true;
}

void StartTask_3_6(int numberOfCircleIterations, int numberOfPointIterations, int numberOfCircles, double r,
                     double ellA, double ellB, double recX, double recY, double rB, double stepX, double epsY)
{
    int countA = 0;
    int countB = 0;

    double **circles = new double* [numberOfCircles];
    for (int i = 0; i < numberOfCircles; i++)
        circles[i] = new double[2];

    for (int i = 0; i < numberOfCircleIterations; i++) {
        for (int j = 0; j < numberOfCircles; j++) {
            while (true) {
                double x;
                double y;
                GetRandomPointInsideOfEllipse(ellA, ellB, &x, &y);

                if (CheckNonIntersection(x, y, r, ellA, ellB, recX, recY, (double(*)[2]) circles, j, stepX, epsY)) {
                    circles[j][0] = x;
                    circles[j][1] = y;
                    break;
                }
            }
        }
        for (int j = 0; j < numberOfPointIterations; j++) {
            double x;
            double y;
            GetRandomPointInsideOfEllipse(ellA, ellB, &x, &y);

            if (CheckIntersectionWithRectangle(x, y, rB, recX, recY))
                countB++;

            for (int k = 0; k < numberOfCircles; k++)
                if (sqrt(pow(x - circles[k][0], 2) + pow(y - circles[k][1], 2)) < r) {
                    countA++;
                    break;
                }
        }
    }

    int numberOfIterations = numberOfCircleIterations * numberOfPointIterations;

    std::cout << "Task 3.6:" << std::endl;
    std::cout << "Result 1: " << (double)countA / numberOfIterations << std::endl;
    std::cout << "Result 2: " << (double)countB / numberOfIterations << std::endl;

    for (int i = 0; i < numberOfCircles; i++)
        delete[] circles[i];

    delete[] circles;
}