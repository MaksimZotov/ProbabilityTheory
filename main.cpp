#include <ctime>
#include <cstdlib>
#include "headers/tasks/Task_2_14.h"
#include "headers/tasks/Task_3_6.h"
#include "headers/tasks/Task_4_34.h"

using namespace std;

void DoTask_2_14() {
    Task_2_14 *task = new Task_2_14();
    task->Start(10000000, 10, 5,2, 3,
                        [](int* countOfFavorableOutcomes, int countOfTakenWinningTickets) -> void
                        {
                            if (countOfTakenWinningTickets == 1) countOfFavorableOutcomes[0]++;
                            if (countOfTakenWinningTickets == 2) countOfFavorableOutcomes[1]++;
                            if (countOfTakenWinningTickets >= 1) countOfFavorableOutcomes[2]++;
                        });
    delete task;
}

void DoTask_3_6() {
    Task_3_6 *task = new Task_3_6();
    task->Start(1000, 1000, 4,2.15,
                       100, 10, 5, 1.5, 5, 0.001, 0.01);
    delete task;
}

void DoTask_4_34() {
    Task_4_34 *task = new Task_4_34();
    task->Start(1000000, 30, 10);
    task->Start(1000000, 30, 5);
    task->Start(1000000, 150, 35);
    delete task;
}


int main() {
    srand(time(NULL));
    DoTask_4_34();
    return 0;
}