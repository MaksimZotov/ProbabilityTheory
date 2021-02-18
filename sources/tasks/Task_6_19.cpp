#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/helpers/Initializer.h"
#include "../../headers/tasks/Task_6_19.h"

void StartTask_6_19(int numberOfIterations, int numberOfHelicopters, double pHelicopter, double pFirstArea)
{
    int *pHelicopters = new int[numberOfHelicopters];
    InitArrayWithZeroes(pHelicopters, numberOfHelicopters);

    for (int i = 0; i < numberOfIterations; i++)
        for (int j = 0; j < numberOfHelicopters; j++) {
            if (GetRandomDouble(0, 1) < pFirstArea) {
                for (int k = 0; k <= j; k++)
                    if (GetRandomDouble(0, 1) <= pHelicopter) {
                        pHelicopters[j]++;
                        break;
                    }
            }
            else {
                for (int k = j + 1; k < numberOfHelicopters; k++)
                    if (GetRandomDouble(0, 1) <= pHelicopter) {
                        pHelicopters[j]++;
                        break;
                    }
                }
        }

    int indexOfMax = 0;
    int max = pHelicopters[indexOfMax];
    for (int i = 1; i < numberOfHelicopters; i++)
        if (pHelicopters[i] > max) {
            max = pHelicopters[i];
            indexOfMax = i;
        }

    std::cout << "Task 6.19:" << std::endl;
    std::cout << "To the first area: " << indexOfMax + 1 << std::endl;
    std::cout << "Probability: " << (double)pHelicopters[indexOfMax] / numberOfIterations << std::endl;

    delete[] pHelicopters;
}