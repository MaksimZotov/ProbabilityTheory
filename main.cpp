#include <ctime>
#include <cstdlib>
#include "headers/tasks/Task_2_14.h"
#include "headers/tasks/Task_3_6.h"

using namespace std;

// Task_2_14:
/*
void CountFavorableOutcomes(int* countOfFavorableOutcomes, int countOfTakenWinningTickets) {
    if (countOfTakenWinningTickets == 1) countOfFavorableOutcomes[0]++;
    if (countOfTakenWinningTickets == 2) countOfFavorableOutcomes[1]++;
    if (countOfTakenWinningTickets >= 1) countOfFavorableOutcomes[2]++;
}

int main() {
    srand(time(NULL));
    Task_2_14 *objTask_2_14 = new Task_2_14();
    objTask_2_14->Start(10000000, 10, 5,
                        2, 3, CountFavorableOutcomes);
    return 0;
}
*/

// Task_3_6:
int main() {
    srand(time(NULL));
    Task_3_6 *objTask_3_6 = new Task_3_6();
    objTask_3_6->Start(1000, 1000, 4,2.15,
                       100, 10, 5, 1.5, 5, 0.001, 0.01);
    return 0;
}