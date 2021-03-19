cmake_minimum_required(VERSION 3.17)
project(ProbabilityTheory)

set(CMAKE_CXX_STANDARD 14)

add_executable(
        ProbabilityTheory
        main.cpp
        sources/helpers/Initializer.cpp
        headers/helpers/Initializer.h
        sources/helpers/NumberGenerator.cpp
        headers/helpers/NumberGenerator.h
        sources/tasks/Task_2_14.cpp
        headers/tasks/Task_2_14.h
        sources/tasks/Task_3_6.cpp
        headers/tasks/Task_3_6.h
        sources/tasks/Task_4_34.cpp
        headers/tasks/Task_4_34.h
        sources/tasks/Task_5_27.cpp
        headers/tasks/Task_5_27.h
        sources/tasks/Task_6_19.cpp
        headers/tasks/Task_6_19.h
        sources/tasks/Task_7_17.cpp
        headers/tasks/Task_7_17.h
        sources/tasks/Task_8_40.cpp
        headers/tasks/Task_8_40.h
        sources/tasks/Task_9_8.cpp
        headers/tasks/Task_9_8.h
        sources/tasks/Task_10_8.cpp headers/tasks/Task_10_8.h sources/tasks/Task_11_3.cpp headers/tasks/Task_11_3.h sources/tasks/Task_12_1.cpp headers/tasks/Task_12_1.h)