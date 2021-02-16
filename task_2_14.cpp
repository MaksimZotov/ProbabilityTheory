#include <ctime>
#include <iostream>
#include <cstdlib>

using namespace std;

// Генерирует случайное целое число в диапазоне [a; b]
int get_random_number(int a, int b) {
    if (a >= b) throw invalid_argument("a must be less than b");
    return rand() % (b - a + 1) + a;
}

int main() {
    srand(time(NULL));

    const int n = 10000000;
    const int number_of_tickets = 10;
    const int number_of_taken_tickets = 5;

    int answer_a = 0;
    int answer_b = 0;
    int answer_c = 0;

    int taken_tickets[number_of_taken_tickets];

    for (int i = 0; i < n; i++) {
        int a = get_random_number(1, number_of_tickets);
        int b = get_random_number(1, number_of_tickets);
        while (b == a) {
            b = get_random_number(1, number_of_tickets);
        }
        for (int j = 0; j < number_of_taken_tickets; j++) {
            while (true) {
                bool again = false;
                int next = get_random_number(1, number_of_tickets);
                for (int k = 0; k < j; k++) {
                    if (taken_tickets[k] == next) {
                        again = true;
                        break;
                    }
                }
                if (!again) {
                    taken_tickets[j] = next;
                    break;
                }
            }
        }
        int count = 0;
        for (int j = 0; j < number_of_taken_tickets; j++) {
            if (taken_tickets[j] == a || taken_tickets[j] == b) {
                count++;
            }
        }
        if (count == 1) answer_a++;
        if (count == 2) answer_b++;
        if (count >= 1) answer_c++;
    }

    cout << (double) answer_a / n << endl;
    cout << (double) answer_b / n << endl;
    cout << (double) answer_c / n << endl;

    return 0;
}