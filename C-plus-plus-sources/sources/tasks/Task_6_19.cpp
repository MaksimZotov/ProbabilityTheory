#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/helpers/Initializer.h"

void StartTask_6_19(int numberOfIterations, int numberOfHelicopters, double pHelicopter, double pFirstArea)
{
    int *pHelicopters = new int[numberOfHelicopters + 1];   // pHelicopters[i] - вероятность найти самолёт,
    InitArrayWithZeroes(pHelicopters, numberOfHelicopters); // если в 1-ый район отправить i вертолётов

    for (int i = 0; i < numberOfIterations; i++)
        // j - количество вертолётов, отправленных в 1-ый район
        for (int j = 0; j <= numberOfHelicopters; j++) {
            // Если самолёт в первом районе
            if (GetRandomDouble(0, 1) < pFirstArea) {
                // Проверяем, удалось ли найти хотя бы одному вертолёту из 1-го района
                for (int k = 1; k <= j; k++)
                    if (GetRandomDouble(0, 1) <= pHelicopter) { // раз удалось, значит, отправление
                        pHelicopters[j]++;                            // j вертолётов в первый район себя
                        break;                                        // оправдало => pHelicopters[j]++
                    }
            }
            // Если самолёт во 2-ом районе
            else {
                // Проверяем, удалось ли найти хотя бы одному вертолёту из 2-го района
                for (int k = j + 1; k <= numberOfHelicopters; k++)
                    if (GetRandomDouble(0, 1) <= pHelicopter) { // раз удалось, значит, отправление
                        pHelicopters[j]++;                            // j вертолётов в первый район себя
                        break;                                        // оправдало => pHelicopters[j]++
                    }
                }
        }

    // Просто ищем макс. вероятность
    int indexOfMax = 0;
    int max = pHelicopters[indexOfMax];
    for (int i = 1; i < numberOfHelicopters; i++)
        if (pHelicopters[i] > max) {
            max = pHelicopters[i];
            indexOfMax = i;
        }

    std::cout << "Task 6.19:" << std::endl;
    std::cout << "To the first area: " << indexOfMax << std::endl;
    std::cout << "Probability: " << (double)pHelicopters[indexOfMax] / numberOfIterations << std::endl;

    delete[] pHelicopters;
}