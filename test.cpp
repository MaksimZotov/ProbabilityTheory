#include <ctime>
#include <iostream>
#include <cstdlib>

using namespace std;

// Генерирует случайное целое число в диапазоне [a; b)
int get_random_number_or_zero(int a, int b) {
    if (a >= b) throw invalid_argument("a must be less than b");
    return rand() % (b - a + 1) + a
}

int main() {
    srand(time(NULL));

    int a = 8;
    int b = 8;
    int array[6] = { 0, 0, 0, 0, 0, 0 };



    for (int i = 0; i < 1000000; i++) {
        int cur = get_random_number_or_zero(a, b);
        array[cur - 1]++;
    }

    for (int i = 0; i < 6; i++)
        cout << array[i] << endl;

    return 0;
}