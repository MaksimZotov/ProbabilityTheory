#include <iostream>
#include "../../headers/helpers/Initializer.h"
#include "../../headers/tasks/Task_2_14.h"

void StartTask_2_14(int numberOfIterations, int numberOfTickets, int numberOfTakenTickets,
                      int numberOfWinningTickets, int numberOfResults, void (*CountFavorableOutcomes) (int*, int))
{
    if (numberOfTickets < numberOfWinningTickets)
        throw "number of tickets must not be less than number of winning tickets";

    if (numberOfTickets < numberOfTakenTickets)
        throw "number of tickets must not be less than number of taken tickets";

    int *countOfFavorableOutcomes = new int[numberOfResults];
    InitArrayWithZeroes(countOfFavorableOutcomes, numberOfResults);

    int *takenTickets = new int[numberOfTakenTickets];
    int *winningTickets = new int[numberOfWinningTickets];

    for (int i = 0; i < numberOfIterations; i++)
    {
        InitArrayWithDifferentRandomNumbers(winningTickets, numberOfWinningTickets, 1, numberOfTickets);
        InitArrayWithDifferentRandomNumbers(takenTickets, numberOfTakenTickets, 1, numberOfTickets);

        int countOfTakenWinningTickets = 0;
        for (int j = 0; j < numberOfTakenTickets; j++)
            for (int k = 0; k < numberOfWinningTickets; k++)
                if (takenTickets[j] == winningTickets[k])
                {
                    countOfTakenWinningTickets++;
                    break;
                }

        CountFavorableOutcomes(countOfFavorableOutcomes, countOfTakenWinningTickets);
    }

    double *results = new double[numberOfResults];
    InitArrayWithZeroes(results, numberOfResults);

    std::cout << "Task 2.14:" << std::endl;
    for (int i = 0; i < numberOfResults; i++) {
        results[i] = (double) countOfFavorableOutcomes[i] / numberOfIterations;
        std::cout << "Result " << i + 1 << ": " << results[i] << std::endl;
    }

    delete[] results;
    delete[] takenTickets;
    delete[] winningTickets;
    delete[] countOfFavorableOutcomes;
}