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
)