#include <ctime>
#include <cstdlib>
#include "headers/tasks/Task_2_14.h"

using namespace std;

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