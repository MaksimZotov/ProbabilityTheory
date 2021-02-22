#include "../../headers/helpers/Initializer.h"
#include "../../headers/helpers/NumberGenerator.h"

void InitArrayWithZeroes(double* array, int n)
{
    for (int i = 0; i < n; i++)
        array[i] = 0;
}

void InitArrayWithZeroes(int* array, int n)
{
    for (int i = 0; i < n; i++)
        array[i] = 0;
}

void InitArrayWithDifferentRandomNumbers(int* array, int n, int a, int b)
{
    if (b - a + 1 < n)
        throw "b - a + 1 must not be less than n";

    for (int j = 0; j < n; j++)
    {
        int next = GetRandomInt(a, b);
        bool again = false;
        for (int k = 0; k < j; k++)
        {
            if (array[k] == next)
            {
                again = true;
                break;
            }
        }
        if (again)
            j--;
        else
            array[j] = next;
    }
}