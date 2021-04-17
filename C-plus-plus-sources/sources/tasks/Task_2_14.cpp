#include <iostream>
#include "../../headers/helpers/Initializer.h"

void StartTask_2_14(int numberOfIterations, int numberOfTickets, int numberOfTakenTickets,
                    int numberOfWinningTickets, int numberOfResults, void (*CountFavorableOutcomes) (int*, int))
{
    if (numberOfTickets < numberOfWinningTickets)
        throw "number of tickets must not be less than number of winning tickets";

    if (numberOfTickets < numberOfTakenTickets)
        throw "number of tickets must not be less than number of taken tickets";

    // Массив для подсчёта количества благоприятных исходов. Один элемет
    // массива равен числу благоприятных исходов конкретного события
    int *countOfFavorableOutcomes = new int[numberOfResults];       // numberOfResults - количество рассматриваемых
    InitArrayWithZeroes(countOfFavorableOutcomes, numberOfResults); // событий (в данной задаче 3 события)

    int *takenTickets = new int[numberOfTakenTickets];     // В задаче numberOfTakenTickets = 5
    int *winningTickets = new int[numberOfWinningTickets]; // В задаче numberOfWinningTickets = 2

    for (int i = 0; i < numberOfIterations; i++)
    {
        // Инициализируем takenTickets и winningTickets разными случайными числами из диапазона
        // [1; numberOfTickets] и [1; numberOfTickets] соответственно (numberOfTickets = 10)
        InitArrayWithDifferentRandomNumbers(winningTickets, numberOfWinningTickets, 1, numberOfTickets);
        InitArrayWithDifferentRandomNumbers(takenTickets, numberOfTakenTickets, 1, numberOfTickets);

        // Проходимся по всем takenTickets и смотрим, совпадает ли взятый билет
        // с одним из winningTickets. Если совпадает, countOfTakenWinningTickets++
        int countOfTakenWinningTickets = 0;
        for (int j = 0; j < numberOfTakenTickets; j++)
            for (int k = 0; k < numberOfWinningTickets; k++)
                if (takenTickets[j] == winningTickets[k])
                {
                    countOfTakenWinningTickets++;
                    break;
                }

        // Зная число выигрышных билетов из взятых, передаем в ламбду void (*CountFavorableOutcomes) (int*, int)
        // массив для подсчёта благоприятных исходов countOfFavorableOutcomes и само значение
        // countOfTakenWinningTickets. В этой лямбде для каждого элемента массива countOfFavorableOutcomes
        // на основе значения countOfTakenWinningTickets будет определено, выполнилось ли на данной итерации
        // событие, соответствующее данному элементу, и, если выполнилось, данный элемент должен увеличиться на 1
        CountFavorableOutcomes(countOfFavorableOutcomes, countOfTakenWinningTickets);
    }

    // Массив результатов (вероятностей событий: results[0] - вероятность в пункте (a), results[1] - в (б) и т.д.)
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