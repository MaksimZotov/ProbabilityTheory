#include <iostream>
#include "../../headers/helpers/Initializer.h"
#include "../../headers/helpers/NumberGenerator.h"

void StartTask_8_40(int numberOfIterations, int numberOfWhite, int numberOfBlack, int maxN, double p)
{
    int numberOfBalls = numberOfWhite + numberOfBlack;

    double *probabilities = new double[maxN]; // probabilities[n-1] - вероятность достать черный шар на n-ом шаге
    InitArrayWithZeroes(probabilities, maxN); // maxN - задаётся пользователем. Если maxN задано слишком малым,
                                              // то Result будет равен -1.

    for (int i = 0; i < numberOfIterations; i++)
        for (int n = 1; n <= maxN; n++)                                   // Для каждого количества шагов n
            for (int j = 1; j <= n; j++)                                  // смотрим, удаётся ли достать
                if (GetRandomInt(1, numberOfBalls) <= numberOfBlack) { // хотя бы раз чёрный шар.
                    probabilities[n - 1]++;                               // Удалось =>
                    break;                                                // => probabilities[n - 1]++
                }

    // Ищём такой наименьший index, что probabilities[index] > p
    int index = -2;
    for (int i = 0; i < maxN; i++) {
        probabilities[i] /= numberOfIterations;
        if (probabilities[i] > p) {
            index = i;
            break;
        }
    }

    std::cout << "Task 8.40:" << std::endl;
    std::cout << "Result: " << index + 1 << std::endl;

    delete[] probabilities;
}