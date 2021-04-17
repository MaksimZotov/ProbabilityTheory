#include <iostream>
#include <math.h>
#include "../../headers/helpers/NumberGenerator.h"

// Генерирует случайную точку (x; y), лежащую в эллипсе с параметрами a = ellA, b = ellB
void GetRandomPointInsideOfEllipse(double ellA, double ellB, double* x, double* y) {
    while (true) {
        *x = GetRandomDouble(-ellA, ellA);
        *y = GetRandomDouble(-ellB, ellB);

        if (*x * *x / (ellA * ellA) + *y * *y / (ellB * ellB) <= 1)
            break;
    }
}

// Проверяет, пересекается ли окружность с центром (x; y) и R = r с прямоугольником
// ширины 2 * recX и высоты 2 * recY, который расположен симметрично относительно (0; 0)
bool CheckIntersectionWithRectangle(double x, double y, double r, double recX, double recY)
{
    double absX = abs(x);
    double absY = abs(y);

    return absX > recX && absY > recY && sqrt(pow(absX - recX, 2) + pow(absY - recY, 2)) <= r ||
           absX < recX && absY - r <= recY || absY < recY && absX - r <= recX;
}

// Проверяет, пересекается ли окружность(x, y, r) с эллипсом(ellA, ellB) или с прямоугольником(recX, recY)
// или с одной из ранее построенных окружностей(circles[][2], n - количество уже построенных окружностей)
bool CheckNonIntersection(double x, double y, double r, double ellA, double ellB, double recX,
                          double recY, double circles[][2], int n, double stepX, double epsY)
{
    // Проверка пересечения с одной из построенных построенных окружностей
    for (int i = 0; i < n; i++)
        if (sqrt(pow(x - circles[i][0], 2) + pow(y - circles[i][1], 2)) < 2 * r)
            return false;

    // Проверка пересечения с прямоугольником
    if (CheckIntersectionWithRectangle(x, y, r, recX, recY))
        return false;

    // Проверка пересечения с эллипсом
    double absX = abs(x); // Проверка сделана через проход по интервалу [|x| - r; |x| + r]
    double absY = abs(y); // c шагом stepX и проверку условия того, что |y(окр(x)) - y(элл(x))| < epsY
    for (double xx = absX - r; xx < absX + r; xx += stepX)
        if (abs((absY + sqrt(pow(r, 2) - pow(xx - absX, 2))) -
                              (ellB * sqrt(1 - pow(absX / ellA, 2)))) < epsY)
            return false;

    return true;
}

void StartTask_3_6(int numberOfCircleIterations, int numberOfPointIterations, int numberOfCircles, double r,
                     double ellA, double ellB, double recX, double recY, double rB, double stepX, double epsY)
{
    int countA = 0; // Счётчик для пункта а)
    int countB = 0; // Счётчик для пункта б)

    double **circles = new double* [numberOfCircles];
    for (int i = 0; i < numberOfCircles; i++)
        circles[i] = new double[2];

    for (int i = 0; i < numberOfCircleIterations; i++) {
        // Генерация окружностей, случайно расположенных внутри эллипса и не пересекающихся с прямоугольником
        for (int j = 0; j < numberOfCircles; j++) {
            while (true) {
                double x;
                double y;
                GetRandomPointInsideOfEllipse(ellA, ellB, &x, &y);

                if (CheckNonIntersection(x, y, r, ellA, ellB, recX, recY,
                                         (double(*)[2]) circles, j, stepX, epsY)) {
                    circles[j][0] = x;
                    circles[j][1] = y;
                    break;
                }
            }
        }
        // Генерация случайных точек внутри эллипса и проверка того, что
        // а) точка лежит в одной из окружностей
        // б) окружность с радиусом rB = 5 см, построенная вокруг этой точки, пересекается с прямоугольником
        for (int j = 0; j < numberOfPointIterations; j++) {
            double x;
            double y;
            GetRandomPointInsideOfEllipse(ellA, ellB, &x, &y);

            for (int k = 0; k < numberOfCircles; k++)
                if (sqrt(pow(x - circles[k][0], 2) + pow(y - circles[k][1], 2)) < r) {
                    countA++;
                    break;
                }

            if (CheckIntersectionWithRectangle(x, y, rB, recX, recY))
                countB++;
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