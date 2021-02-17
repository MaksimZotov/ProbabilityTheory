#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"

int getRandomInt(int a, int b) {
    if (a >= b) throw std::invalid_argument("a must be less than b");
    return rand() % (b - a + 1) + a;
}

double getRandomDouble(double a, double b) {
    if (a > b) throw std::invalid_argument("a must be less than b or equal to b");
    return (a == b) ? 0 : ((b - a) * ((double)rand() / RAND_MAX)) + a;
}