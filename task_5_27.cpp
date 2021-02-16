#include <ctime>
#include <iostream>
#include <cstdlib>
#include <math.h>

using namespace std;

// Генерирует случайное действительное число в диапазоне [a; b]
double get_random_number(double a, double b) {
    if (a > b) throw invalid_argument("a must be less than b or equal to b");
    return (a == b) ? 0 : ((b - a) * ((double)rand() / RAND_MAX)) + a;
}

int main() {
    srand(time(NULL));
    const int number_of_iterations = 1000000;
    const double p1 = 0.2;
    const double p2 = 0.3;
    int count = 0;
    for (int i = 0; i < number_of_iterations; i++) {
        while (true) {
            if (get_random_number(0, 1) <= p1) {
                count++;
                break;
            }
            if (get_random_number(0, 1) <= p2) {
                break;
            }
        }
    }
    cout << "\nResult: " << (double)count / number_of_iterations << endl;
}