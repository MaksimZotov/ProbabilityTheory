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
    const int number_of_iterations = 10000000;
    const int number_of_butches_with_parts = 3;
    const double percent_of_second_rate_parts = 1.0 / 3;
    int count1 = 0;
    int count2 = 0;
    int n = 0;
    for (int i = 0; i < number_of_iterations; i++) {
        int butch_with_second_rate_parts = get_random_number(1, number_of_butches_with_parts);
        int chosen_butch = get_random_number(1, number_of_butches_with_parts);
        if (butch_with_second_rate_parts == chosen_butch) {
            if (get_random_number(0.0, 1.0) > percent_of_second_rate_parts) count1++;
            else n++;
            count2 += (get_random_number(0, 1) > percent_of_second_rate_parts) ? 1 : 0;
        }
    }
    cout << (double)count1 / (number_of_iterations - n) << endl;

    // incorrect result: actual ~ 0.187, expected ~ 0.182
    cout << (double)count2 / (number_of_iterations - n) << endl;
}