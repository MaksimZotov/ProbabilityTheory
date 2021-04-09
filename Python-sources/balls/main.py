import plotly.graph_objs as go
import numpy as np
import copy
import re

N = 290
m = 6
limit = 5000

H = [[1 / (N + 1) for i in range(N + 1)] for j in range(m)]
removedCombinations = []
colors = ['Red', 'White', 'Black', 'Green', 'Blue', 'Yellow']



with open('Python-sources/balls/task_1_balls.txt') as line:
    countExp = 0

    while True:
        data = re.split(' |, |\n', line.readline())

        if len(data) != 0 and data[0] == '#':
            if len(data) == 6:
                quantityOfTakenBalls = 2
            elif len(data) == 7:
                quantityOfTakenBalls = 3
            else:
                break

            A_I_Hj = [[0 for i in range(N + 1)] for j in range(m)]
            nA_I_Hj = [[0 for i in range(N + 1)] for j in range(m)]
            Hj_I_A = [[0 for i in range(N + 1)] for j in range(m)]
            Hj_I_nA = [[0 for i in range(N + 1)] for j in range(m)]

            ki = [0] * m
            for i in range(len(data) - quantityOfTakenBalls - 1, len(data) - 1):
                ki[colors.index(data[i])] += 1

            for i in range(m):
                if ki[i] > 0:
                    for j in range(N + 1):
                        A_I_Hj[i][j] += (j / N) ** ki[i]
                else:
                    for j in range(N + 1):
                        nA_I_Hj[i][j] += (N - j) / N

            for i in range(m):
                if ki[i] > 0:
                    E = 0
                    for j in range(N + 1):
                        E += H[i][j] * A_I_Hj[i][j]
                    for j in range(N + 1):
                        Hj_I_A[i][j] += H[i][j] * A_I_Hj[i][j] / E
                else:
                    E = 0
                    for j in range(N + 1):
                        E += H[i][j] * nA_I_Hj[i][j]
                    for j in range(N + 1):
                        Hj_I_nA[i][j] += H[i][j] * nA_I_Hj[i][j] / E

            for i in range(m):
                if ki[i] > 0:
                    for j in range(N + 1):
                        H[i][j] = Hj_I_A[i][j]
                else:
                    for j in range(N + 1):
                        H[i][j] = Hj_I_nA[i][j]

            #test = [0] * m
            #for i in range(m):
            #    for j in range(N + 1):
            #        test[i] += H[i][j]
            #for i in range(m):
            #    print(test[i], ' ')
            #print('\n')

            countExp += 1
            if countExp > limit:
                break




