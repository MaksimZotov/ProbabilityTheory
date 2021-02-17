#include <ctime>
#include <iostream>
#include <cstdlib>
#include <math.h>

using namespace std;

// Генерирует случайное целое число в диапазоне [a; b]
int get_random_number(int a, int b) {
    if (a >= b) throw invalid_argument("a must be less than b");
    return rand() % (b - a + 1) + a;
}

int main() {
    srand(time(NULL));
    const int number_of_iterations = 100000;
    const int a = 100;
    const int b = 1000;
    int count_uneven = 0;
    int count = 0;
    for (int i = 0; i < number_of_iterations; i++) {
        int n = get_random_number(a, b);
        for (int j = 0; j < n; j++) {
            count_uneven += get_random_number(0, 1) == 1 ? 1 : 0;
        }
        if (count_uneven % 2 == 1) {
            count++;
        }
    }
    cout << (double)count / number_of_iterations << endl;
}