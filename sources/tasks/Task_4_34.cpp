#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_4_34.h"

using namespace std;

void Task_4_34::Start(int numberOfIterations, int n, int m)
{
    if (2 * m > n + 1)
        throw "2 * m must not be greater than n + 1";

    int count = 0;
    int *queue = new int[n + m];
    for (int i = 0; i < numberOfIterations; i++) {
        int a = 1;
        int b = n + m;
        for (int j = 0; j < n + m; j++) {
            if (a == b)
                queue[j] = a > m ? 1 : 3;
            else {
                queue[j] = getRandomInt(a, b) > m ? 1 : 3;
                if (queue[j] == 1)
                    b--;
                else
                    a++;
            }
        }
        int countN = 0;
        for (int j = 0; j < n + m; j++) {
            if (queue[j] == 1)
                countN++;
            else if (countN >= 2)
                countN -= 2;
            else {
                count++;
                break;
            }
        }
    }
    cout << "\nResult: " << 1 - (double)count / numberOfIterations << endl;
    delete[] queue;
}
