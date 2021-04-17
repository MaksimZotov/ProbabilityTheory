#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"

void StartTask_5_27(int numberOfIterations, double p1, double p2) {
    int count = 0;

    for (int i = 0; i < numberOfIterations; i++) {
        while (true) {
            if (GetRandomDouble(0, 1) <= p1) { // Если 1-ый стрелок попал первым, то он, судя по условию
                count++;                             // задачи, сделает больше выстрелов => увеличиваем count на 1
                break;
            }
            if (GetRandomDouble(0, 1) <= p2)   // Если 2-ой стрелок попал первым, то 1-ый уже никак не
                break;                               // сможет сделать больше выстрелов => след. итерация
        }
    }

    std::cout << "Task 5.27:" << std::endl;
    std::cout << "Result: " << (double)count / numberOfIterations << std::endl;
}
