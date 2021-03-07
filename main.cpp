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

int main() {
    srand(time(NULL));

    StartTask_2_14(10000000, 10, 5, 2, 3,
                   [](int* countOfFavorableOutcomes, int countOfTakenWinningTickets) -> void
                   {
                       if (countOfTakenWinningTickets == 1) countOfFavorableOutcomes[0]++;
                       if (countOfTakenWinningTickets == 2) countOfFavorableOutcomes[1]++;
                       if (countOfTakenWinningTickets >= 1) countOfFavorableOutcomes[2]++;
                   }
    );

    StartTask_3_6(1000, 1000, 4, 2.15, 100, 10, 5, 1.5, 5, 0.001, 0.01);

    StartTask_4_34(1000000, 30, 10);
    StartTask_4_34(1000000, 30, 5);
    StartTask_4_34(1000000, 50, 15);

    StartTask_5_27(1000000, 0.2, 0.3);

    StartTask_6_19(1000000, 10, 0.2, 0.8);

    StartTask_7_17(10000000, 3, 1.0 / 3);

    StartTask_8_40(1000000, 20, 2, 20, 0.5);

    StartTask_9_8(1000000, 100, 1000);

    return 0;
}