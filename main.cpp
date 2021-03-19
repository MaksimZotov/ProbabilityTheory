#include <ctime>
#include <cstdlib>
#include "headers/tasks/Task_12_1.h"

int main() {
    srand(time(NULL));

    // Пункт а)
    StartTask_12_1(
            0.5, 0.0001,
            [](double x) -> double { return (x >= 0 && x <= 1) ? 1 : 0; },
            [](double x) -> double
            {
                if (x < 0) return 0;
                if (x > 1) return 1;
                return x;
            }
    );

    // Пункт б)
    StartTask_12_1(
            5, 0.0001,
            [](double x) -> double { return exp(- x * x / 2) * 0.39894228; }, // 0.39894228 =
            [](double x) -> double                                             // = 1 / (2 * pi)^(1/2)
            {
                double integral = 0;
                double h = 0.0001;
                for (double t = -100; t < x; t += h)
                    integral += exp(- t * t / 2) * h;
                return integral * 0.39894228; // 0.39894228 = 1 / (2 * pi)^(1/2)
            }
    );
    return 0;
}


