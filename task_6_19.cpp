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
    const int number_of_helicopters = 10;
    const double p_helicopter = 0.2;
    const double p_first_area = 0.8;
    int p_helicopters[number_of_helicopters];
    for (int i = 0; i < number_of_helicopters; i++) {
        p_helicopters[i] = 0;
    }
    for (int i = 0; i < number_of_iterations; i++) {
        for (int j = 0; j < number_of_helicopters; j++) {
            bool first_area = get_random_number(0, 1) < p_first_area;
            if (first_area) {
                for (int k = 0; k <= j; k++) {
                    if (get_random_number(0, 1) <= p_helicopter) {
                        p_helicopters[j]++;
                        break;
                    }
                }
            } else {
                for (int k = j + 1; k < number_of_helicopters; k++) {
                    if (get_random_number(0, 1) <= p_helicopter) {
                        p_helicopters[j]++;
                        break;
                    }
                }
            }
        }
    }
    int index_of_max = 0;
    int max = p_helicopters[index_of_max];
    for (int i = 1; i < number_of_helicopters; i++) {
        if (p_helicopters[i] > max) {
            max = p_helicopters[i];
            index_of_max = i;
        }
    }
    for (int i = 0; i < number_of_helicopters; i++) {
        cout << i + 1 << ": " << (double)p_helicopters[i] / number_of_iterations << endl;
    }
    cout << "Number of helicopters to the first area: " << index_of_max + 1 << endl;
    cout << "Probability: " << (double)p_helicopters[index_of_max] / number_of_iterations << endl;
}