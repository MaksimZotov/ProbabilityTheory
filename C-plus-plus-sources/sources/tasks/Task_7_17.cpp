#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"

void StartTask_7_17(int numberOfIterations, int numberOfBatches, double percentOfSecondRate)
{
    int count1 = 0; // Число случаев, когда 1-ая взятая деталь, оказавшаяся
                    // 1-сортной, была взята из партии с 2-сортными деталями

    int n1 = 0;     // Число случаев, когда 1-ая взятая деталь оказалась 1-сортной

    int count2 = 0; // Число случаев, когда 1-ая взятая деталь, оказавшаяся
                    // 1-сортной И ВЗЯТОЙ ИЗ ПАРТИИ С 2-СОРТНЫМИ ДЕТАЛЯМИ, была
                    // возвращена обратно в свою партию и после повторного взятия
                    // детяли из той же партии была взята 1-сортная деталь

    int n2 = 0;     // Число случаев, когда 1-ая взятая деталь, оказавшаяся
                    // 1-сортной ....................................... , была
                    // возвращена обратно в свою партию и после повторного взятия
                    // детяли из той же партии была взята 1-сортная деталь

    for (int i = 0; i < numberOfIterations; i++) {
        int butchWithSecondRate = GetRandomInt(1, numberOfBatches);
        int chosenBatch = GetRandomInt(1, numberOfBatches);
        if (butchWithSecondRate == chosenBatch) {
            if (GetRandomDouble(0, 1) > percentOfSecondRate) {
                count1++;
                n1++;
                if (GetRandomDouble(0, 1) > percentOfSecondRate) {
                    count2++;
                    n2++;
                }
            }
        }
        else {
            n1++;
            n2++;
        }
    }

    std::cout << "Task 7.17:" << std::endl;
    std::cout << "Result 1: " << (double)count1 / n1 << std::endl;
    std::cout << "Result 2: " << (double)count2 / n2 << std::endl;
}