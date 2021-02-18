#ifndef PROBABILITYTHEORY_TASK_2_14_H
#define PROBABILITYTHEORY_TASK_2_14_H

class Task_2_14
{
private:
    void ShowResults(double *results, int n);

public:
    void Start(int numberOfIterations, int numberOfTickets, int numberOfTakenTickets,
               int numberOfWinningTickets, int numberOfResults, void (*CountFavorableOutcomes) (int*, int));
};

#endif
