#include <iostream>
#include "../../headers/helpers/Initializer.h"
#include "../../headers/tasks/Task_2_14.h"

using namespace std;

Task_2_14::Task_2_14() { }

void Task_2_14::ShowResults(double *results, int n)
{
    for (int i = 0; i < n; i++)
        cout << "result " << i + 1 << ": " << results[i] << endl;
}

void Task_2_14::Start(int numberOfIterations, int numberOfTickets, int numberOfTakenTickets,
                     int numberOfWinningTickets, int numberOfResults, void (*CountFavorableOutcomes) (int*, int))
{
    if (numberOfTickets < numberOfWinningTickets) throw "number of tickets must not be less than number of winning tickets";
    if (numberOfTickets < numberOfTakenTickets) throw "number of tickets must not be less than number of taken tickets";

    int *countOfFavorableOutcomes = new int[numberOfResults];
    InitArrayWithZeroes(countOfFavorableOutcomes, numberOfResults);

    int *takenTickets = new int[numberOfTakenTickets];
    int *winningTickets = new int[numberOfWinningTickets];

    for (int i = 0; i < numberOfIterations; i++)
    {
        InitArrayWithRandomNumbers(winningTickets, numberOfWinningTickets, 1, numberOfTickets);
        InitArrayWithRandomNumbers(takenTickets, numberOfTakenTickets, 1, numberOfTickets);

        int countOfTakenWinningTickets = 0;
        for (int j = 0; j < numberOfTakenTickets; j++)
            for (int k = 0; k < numberOfWinningTickets; k++)
                if (takenTickets[j] == winningTickets[k])
                    countOfTakenWinningTickets++;

        CountFavorableOutcomes(countOfFavorableOutcomes, countOfTakenWinningTickets);
    }

    double *results = new double[numberOfResults];
    InitArrayWithZeroes(results, numberOfResults);

    for (int i = 0; i < numberOfResults; i++)
        results[i] = (double)countOfFavorableOutcomes[i] / numberOfIterations;

    ShowResults(results, numberOfResults);

    delete[] countOfFavorableOutcomes;
    delete[] results;
    delete[] takenTickets;
    delete[] winningTickets;
}