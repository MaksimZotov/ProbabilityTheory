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

bool check_intersection_with_rectangle(double x, double y, double r, double rec_x, double rec_y) {
    double abs_x = abs(x);
    double abs_y = abs(y);

    return abs_x > rec_x && abs_y > rec_y && sqrt(pow(abs_x - rec_x, 2) + pow(abs_y - rec_y, 2)) <= r ||
           abs_x < rec_x && abs_y - r <= rec_y || abs_y < rec_y && abs_x - r <= rec_x;
}

bool check_non_intersection(double x, double y, double r, double ell_a, double ell_b, double rec_x,
                            double rec_y, double circles[][2], int n, double step_x, double eps_y) {
    for (int i = 0; i < n; i++) {
        if (sqrt(pow(x - circles[i][0], 2) + pow(y - circles[i][1], 2)) < 2 * r) {
            return false;
        }
    }

    if (check_intersection_with_rectangle(x, y, r, rec_x, rec_y)) {
        return false;
    }

    double abs_x = abs(x);
    double abs_y = abs(y);
    for (double xx = abs_x - r; xx < abs_x + r; xx += step_x) {
        if (abs((abs_y + sqrt(pow(r, 2) - pow(xx - abs_x, 2))) - (ell_b * sqrt(1 - pow(abs_x / ell_a, 2)))) < eps_y) {
            return false;
        }
    }

    return true;
}

int main() {
    srand(time(NULL));

    const int number_of_circle_iterations = 10000;
    const int number_of_point_iterations = 1000;

    const int number_of_circles = 4;
    const double ell_a = 100;
    const double ell_b = 10;
    const double rec_x = 1.5;
    const double rec_y = 5;
    const double r = 2.15;
    const double r_b = 5;
    const double step_x = 0.001;
    const double eps_y = 0.01;

    int count_a = 0;
    int count_b = 0;

    double circles[number_of_circles][2];

    for (int i = 0; i < number_of_circle_iterations; i++) {
        for (int j = 0; j < number_of_circles; j++) {
            while (true) {
                double x;
                double y;
                while (true) {
                    x = get_random_number(-ell_a, ell_a);
                    y = get_random_number(-ell_b, ell_b);
                    if (x * x / (ell_a * ell_a) + y * y / (ell_b * ell_b) <= 1) {
                        break;
                    }
                }
                if (check_non_intersection(x, y, r, ell_a, ell_b, rec_x, rec_y, (double(*)[2]) circles, j, step_x, eps_y)) {
                    circles[j][0] = x;
                    circles[j][1] = y;
                    break;
                }
            }
        }
        for (int j = 0; j < number_of_point_iterations; j++) {
            double x = get_random_number(-ell_a, ell_a);
            double y = get_random_number(-ell_b, ell_b);
            if (x * x / (ell_a * ell_a) + y * y / (ell_b * ell_b) > 1) {
                j--;
                continue;
            }
            if (check_intersection_with_rectangle(x, y, r_b, rec_x, rec_y)) {
                count_b++;
            }
            for (int k = 0; k < number_of_circles; k++) {
                if (sqrt(pow(x - circles[k][0], 2) + pow(y - circles[k][1], 2)) < r) {
                    count_a++;
                    break;
                }
            }
        }
    }

    int number_of_iterations = number_of_circle_iterations * number_of_point_iterations;
    cout << (double)count_a / number_of_iterations << endl;
    cout << (double)count_b / number_of_iterations << endl;

    return 0;
}