#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"

// Случайное целое число из диапазона [a; b]
int GetRandomInt(int a, int b) {
    if (a >= b)
        throw "a must be less than b";

    return rand() % (b - a + 1) + a;
}

// Случайное вещественное число из диапазона [a; b]
double GetRandomDouble(double a, double b) {
    if (a > b)
        throw "a must be less than b or equal to b";

    return (a == b) ? 0 : ((b - a) * ((double)rand() / RAND_MAX)) + a;
}