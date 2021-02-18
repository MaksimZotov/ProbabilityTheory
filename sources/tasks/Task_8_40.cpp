#include <iostream>
#include "../../headers/helpers/Initializer.h"
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_8_40.h"

void StartTask_8_40(int numberOfIterations, int numberOfWhite, int numberOfBlack, int maxN, double p)
{
    int numberOfBalls = numberOfWhite + numberOfBlack;

    double *probabilities = new double[maxN];
    InitArrayWithZeroes(probabilities, maxN);

    for (int i = 0; i < numberOfIterations; i++)
        for (int n = 1; n <= maxN; n++)
            for (int j = 1; j <= n; j++)
                if (GetRandomInt(1, numberOfBalls) <= numberOfBlack) {
                    probabilities[n - 1]++;
                    break;
                }

    int index;
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