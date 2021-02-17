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
    const int number_of_iterations = 10000;
    const int number_of_white = 20;
    const int number_of_black = 2;
    const int max_n = 20;
    const double p = 0.5;
    int number_of_balls = number_of_white + number_of_black;
    double probabilities[max_n];
    for (int i = 0; i < max_n; i++) {
        probabilities[i] = 0;
    }
    for (int i = 0; i < number_of_iterations; i++) {
        for (int n = 1; n <= max_n; n++) {
            for (int j = 1; j <= n; j++) {
                if (get_random_number(1, number_of_balls) <= number_of_black) {
                    probabilities[n - 1]++;
                    break;
                }
            }
        }
    }
    int index;
    for (int i = 0; i < max_n; i++) {
        probabilities[i] /= number_of_iterations;
        if (probabilities[i] > p) {
            index = i;
            break;
        }
    }
    cout << "Min N: " << index + 1 << endl;
}