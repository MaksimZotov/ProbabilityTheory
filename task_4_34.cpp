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

    // 2m <= n + 1
    const int number_of_iterations = 100000;
    const int n = 10; // 1-рублевые
    const int m = 3;  // 3-рублевые

    int count = 0;



    int queue[n + m];
    int checker_n[n + m];
    int checker_m[n + m];
    for (int i = 0; i < n + m; i++) {
        checker_n[i] = 0;
        checker_m[i] = 0;
    }
    for (int i = 0; i < number_of_iterations; i++) {
        int count_n = 0;
        int count_m = 0;
        for (int j = 0; j < n + m; j++) {
            if (count_n == n) {
                queue[j] = 3;
                checker_m[j]++;
                continue;
            } else if (count_m == m) {
                queue[j] = 1;
                checker_n[j]++;
                continue;
            }
            if (get_random_number(0, 1) == 0) {
                queue[j] = 1;
                checker_n[j]++;
                count_n++;
            } else {
                queue[j] = 3;
                checker_m[j]++;
                count_m++;
            }
        }
        count_n = 0;
        for (int j = 0; j < n + m; j++) {
            if (queue[j] == 1) {
                count_n++;
            } else if (count_n < 2) {
                count++;
                break;
            } else {
                count_n -= 2;
            }
        }
    }
    cout << "\nResult: " << (double)count / number_of_iterations << endl;
    for (int i = 0; i < n + m; i++) {
        cout << "n[" << i << "] = " << checker_n[i] << " m[" << i << "] = " << checker_m[i] << endl;
    }
}

/*
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

    // 2m <= n + 1
    const int number_of_iterations = 10000;
    const int n = 10; // 1-рублевые
    const int m = 3;  // 3-рублевые

    int count = 0;



    int *queue;
    int checker_n[n + m];
    int checker_m[n + m];
    for (int i = 0; i < n + m; i++) {
        checker_n[i] = 0;
        checker_m[i] = 0;
    }
    for (int i = 0; i < number_of_iterations; i++) {
        int count_n = 0;
        int count_m = 0;
        queue = new int[n + m];
        while (count_n + count_m != n + m) {
            int next_index = get_random_number(0, n + m - 1);
            if (queue[next_index] == 3 || queue[next_index] == 1) {
                continue;
            }
            int next_number = get_random_number(0, 1) == 0 ? 1 : 3;
            if (next_number == 1) {
                if (count_n == n) {
                    continue;
                }
                count_n++;
            }
            else {
                if (count_m == m) {
                    continue;
                }
                count_m++;
            }
            queue[next_index] = next_number;
        }

        for (int j = 0; j < n + m; j++) {
            if (queue[j] == 1) checker_n[j]++;
            else checker_m[j]++;
        }

        count_n = 0;
        for (int j = 0; j < n + m; j++) {
            if (queue[j] == 1) {
                count_n++;
            } else if (count_n < 2) {
                count++;
                break;
            } else {
                count_n -= 2;
            }
        }
        //cout << "----------" << endl;
        //for (int j = 0; j < n + m; j++) {
        //    cout << queue[j] << endl;
        //}
        //cout << "----------" << endl;
        delete[] queue;
    }
    cout << "\nResult: " << (double)count / number_of_iterations << endl;
    for (int i = 0; i < n + m; i++) {
        cout << "n[" << i << "] = " << checker_n[i] << " m[" << i << "] = " << checker_m[i] << endl;
    }
}
 */

/*
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

    // 2m <= n + 1
    const int number_of_iterations = 10000;
    const int n = 10; // 1-рублевые
    const int m = 3;  // 3-рублевые

    int count = 0;



    int *queue;
    int checker_n[n + m];
    int checker_m[n + m];
    for (int i = 0; i < n + m; i++) {
        checker_n[i] = 0;
        checker_m[i] = 0;
    }
    for (int i = 0; i < number_of_iterations; i++) {
        queue = new int[n + m];

        int a = 1;
        int b = n + m;
        for (int j = 0; j < n + m; j++) {
            if (a == b) {
                queue[j] = a > m ? 1 : 3;
            } else {
                int next = get_random_number(a, b);
                if (next > m) {
                    queue[j] = 1;
                    b--;
                } else {
                    queue[j] = 3;
                    a++;
                }
            }
        }

        for (int j = 0; j < n + m; j++) {
            if (queue[j] == 1) checker_n[j]++;
            else checker_m[j]++;
        }

        int count_n = 0;
        for (int j = 0; j < n + m; j++) {
            if (queue[j] == 1) {
                count_n++;
            } else if (count_n < 2) {
                count++;
                break;
            } else {
                count_n -= 2;
            }
        }
        //cout << "----------" << endl;
        //for (int j = 0; j < n + m; j++) {
        //    cout << queue[j] << endl;
        //}
        //cout << "----------" << endl;
        delete[] queue;
    }
    cout << "\nResult: " << (double)count / number_of_iterations << endl;
    for (int i = 0; i < n + m; i++) {
        cout << "n[" << i << "] = " << checker_n[i] << " m[" << i << "] = " << checker_m[i] << endl;
    }
}
 */