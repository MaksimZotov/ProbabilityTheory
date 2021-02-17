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

// Генерирует случайное действительное число в диапазоне [a; b]
double get_random_number(double a, double b) {
    if (a > b) throw invalid_argument("a must be less than b or equal to b");
    return (a == b) ? 0 : ((b - a) * ((double)rand() / RAND_MAX)) + a;
}

int main() {
    srand(time(NULL));
    const int number_of_iterations = 100;
    const int number_of_white = 20;
    const int number_of_black = 2;
    const int max_n = 20;
    const double p = 0.5;
    int number_of_balls = number_of_white + number_of_black;
    int probabilities[max_n];
    for (int i = 0; i < max_n; i++) {
        probabilities[i] = 0;
    }
    for (int i = 0; i < number_of_iterations; i++) {
        for (int n = 1; n <= max_n; n++) {
            bool stop = false;
            for (int j = 1; j <= n; j++) {
                if (get_random_number(1, number_of_balls) <= number_of_black) {
                    if ((double)j / n > p) {
                        probabilities[n - 1]++;
                        stop = true;
                        break;
                    }
                }
            }
            if (stop) break;
        }
    }
    int index_of_max = 0;
    int max = probabilities[index_of_max];
    for (int i = 0; i < max_n; i++) {
        if (probabilities[i] > max) {
            max = probabilities[i];
            index_of_max = i;
        }
    }
    cout << "Min N: " << index_of_max + 1 << endl;
}