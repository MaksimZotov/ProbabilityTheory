#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"

void StartTask_4_34(int numberOfIterations, int n, int m)
{
    if (2 * m > n + 1)
        throw "2 * m must not be greater than n + 1";

    int count = 0;
    int *queue = new int[n + m];

    for (int i = 0; i < numberOfIterations; i++) {
        int a = 1;
        int b = n + m;
        // Заполнение очереди
        for (int j = 0; j < n + m; j++) {
            if (a == b)                                    // Так как есть n человек с 1-рублёвками и m человек
                queue[j] = a > m ? 1 : 3;                  // с 3-рублёвками, вероятнось того, что первый в
            else {                                         // очереди человек с 1-рублёвками, равна n / (n + m).
                queue[j] = GetRandomInt(a, b) > m ? 1 : 3; // Если оказалось, что первый в очереди с 1-рубл.
                if (queue[j] == 1)                         // то вероятность P2 того, что человек с 1-рубл.
                    b--;                                   // второй в очереди, равна (n-1) / (n-1 + m)
                else                                       // Если же первый в очереди с 3-рубл., то
                    a++;                                   // та же вероятность P2 равна n / (n + m-1).
            }                                              // Приведённый слева способ заполнения очереди
        }                                                  // учитывает сказанное выше
        int countN = 0; // Количество 1-рублёвок в кассе
        for (int j = 0; j < n + m; j++) {
            if (queue[j] == 1)    // Если queue[j] == 1, то пришел с 1-рубл.
                countN++;
            else if (countN >= 2) // Если queue[j] != 1, то пришел с 3-рубл.
                countN -= 2;      // и ему надо дать 2 рубля сдачи
            else {       // Если двух рублей в кассе нет, то
                count++; // увелчиваем счётчик ситуаций, когда людям пришлось ждать
                break;
            }
        }
    }

    std::cout << "Task 4.34:" << std::endl;
    std::cout << "Result: " << 1 - (double)count / numberOfIterations << std::endl;

    delete[] queue;
}
