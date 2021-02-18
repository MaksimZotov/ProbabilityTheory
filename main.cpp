#include <ctime>
#include <cstdlib>
#include "headers/tasks/Task_2_14.h"
#include "headers/tasks/Task_3_6.h"
#include "headers/tasks/Task_4_34.h"
#include "headers/tasks/Task_5_27.h"
#include "headers/tasks/Task_6_19.h"
#include "headers/tasks/Task_7_17.h"
#include "headers/tasks/Task_8_40.h"
#include "headers/tasks/Task_9_8.h"

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

void DoTask_5_27() {
    Task_5_27 *task = new Task_5_27();
    task->Start(1000000, 0.2, 0.3);
    delete task;
}

void DoTask_6_19() {
    Task_6_19 *task = new Task_6_19();
    task->Start(1000000, 10, 0.2, 0.8);
    delete task;
}

void DoTask_7_17() {
    Task_7_17 *task = new Task_7_17();
    task->Start(10000000, 3, 1.0 / 3);
    delete task;
}

void DoTask_8_40() {
    Task_8_40 *task = new Task_8_40();
    task->Start(1000000, 20, 2, 20, 0.5);
    delete task;
}

void DoTask_9_8() {
    Task_9_8 *task = new Task_9_8();
    task->Start(1000000, 100, 1000);
    delete task;
}

int main() {
    srand(time(NULL));
    // DoTask_m_n();
    return 0;
}