cmake_minimum_required(VERSION 3.17)
project(ProbabilityTheory)

set(CMAKE_CXX_STANDARD 14)

add_executable(
        ProbabilityTheory
        C-plus-plus-sources/main.cpp
        C-plus-plus-sources/sources/helpers/Initializer.cpp
        C-plus-plus-sources/headers/helpers/Initializer.h
        C-plus-plus-sources/sources/helpers/NumberGenerator.cpp
        C-plus-plus-sources/headers/helpers/NumberGenerator.h
        C-plus-plus-sources/sources/tasks/Task_2_14.cpp
        C-plus-plus-sources/headers/tasks/Task_2_14.h
        C-plus-plus-sources/sources/tasks/Task_3_6.cpp
        C-plus-plus-sources/headers/tasks/Task_3_6.h
        C-plus-plus-sources/sources/tasks/Task_4_34.cpp
        C-plus-plus-sources/headers/tasks/Task_4_34.h
        C-plus-plus-sources/sources/tasks/Task_5_27.cpp
        C-plus-plus-sources/headers/tasks/Task_5_27.h
        C-plus-plus-sources/sources/tasks/Task_6_19.cpp
        C-plus-plus-sources/headers/tasks/Task_6_19.h
        C-plus-plus-sources/sources/tasks/Task_7_17.cpp
        C-plus-plus-sources/headers/tasks/Task_7_17.h
        C-plus-plus-sources/sources/tasks/Task_8_40.cpp
        C-plus-plus-sources/headers/tasks/Task_8_40.h
        C-plus-plus-sources/sources/tasks/Task_9_8.cpp
        C-plus-plus-sources/headers/tasks/Task_9_8.h
        C-plus-plus-sources/sources/tasks/Task_10_8.cpp
        C-plus-plus-sources/headers/tasks/Task_10_8.h
        C-plus-plus-sources/sources/tasks/Task_11_3.cpp
        C-plus-plus-sources/headers/tasks/Task_11_3.h
        C-plus-plus-sources/sources/tasks/Task_12_1.cpp
        C-plus-plus-sources/headers/tasks/Task_12_1.h)