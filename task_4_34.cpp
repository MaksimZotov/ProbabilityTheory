#include <ctime>
#include <iostream>
#include <cstdlib>
#include <math.h>

using namespace std;

int get_random_number(int a, int b) {
    if (a >= b) throw invalid_argument("a must be less than b");
    return rand() % (b - a + 1) + a;
}

int main() {
    srand(time(NULL));
    const int number_of_iterations = 1000000;
    const int n = 30;
    const int m = 10;
    int count = 0;
    int *queue;
    for (int i = 0; i < number_of_iterations; i++) {
        queue = new int[n + m];
        int a = 1;
        int b = n + m;
        for (int j = 0; j < n + m; j++) {
            if (a == b) queue[j] = a > m ? 1 : 3;
            else {
                queue[j] = get_random_number(a, b) > m ? 1 : 3;
                if (queue[j] == 1) b--;
                else a++;
            }
        }
        int count_n = 0;
        for (int j = 0; j < n + m; j++) {
            if (queue[j] == 1)count_n++;
            else if (count_n >= 2) count_n -= 2;
            else {
                count++;
                break;
            }
        }
        delete[] queue;
    }
    cout << "\nResult: " << 1 - (double)count / number_of_iterations << endl;
}