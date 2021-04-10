import plotly.graph_objs as go
import numpy as np
import copy
import re

N = 290
m = 6
limit = 9100


H = [[1 / (N + 1) for i in range(N + 1)] for j in range(m)]
colors = ['Red', 'White', 'Black', 'Green', 'Blue', 'Yellow']

steps = 29
sliderSteps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20,
               30, 40, 50,  100, 200, 300, 400, 500, 1000, 2000, 4000, 9000]
output = []

quantityWithMaxProb = [[] for i in range(m)]

countTakenBallsAll = 0
countTakenBalls = [0] * m
quantityBasedOnFrequency = [[] for i in range(m)]

countColors = [[] for i in range(m)]
minP = 0.000001

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

            for i in range(m):
                count = 0
                for j in range(N + 1):
                    if H[i][j] > minP:
                        count += 1
                countColors[i].append(count)

            sliderStepsContainsCountExp = sliderSteps.__contains__(countExp)

            if sliderStepsContainsCountExp:
                output.append(copy.deepcopy(H))
                for i in range(m):
                    quantityWithMaxProb[i].append(H[i].index(max(H[i])))

            A_I_Hj = [[0 for i in range(N + 1)] for j in range(m)]
            nA_I_Hj = [[0 for i in range(N + 1)] for j in range(m)]
            Hj_I_A = [[0 for i in range(N + 1)] for j in range(m)]
            Hj_I_nA = [[0 for i in range(N + 1)] for j in range(m)]

            ki = [0] * m
            for i in range(len(data) - quantityOfTakenBalls - 1, len(data) - 1):
                ki[colors.index(data[i])] += 1

                countTakenBalls[colors.index(data[i])] += 1
            countTakenBallsAll += quantityOfTakenBalls
            if sliderStepsContainsCountExp:
                for i in range(m):
                    quantityBasedOnFrequency[i].append((countTakenBalls[i] / countTakenBallsAll) * N)

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

            countExp += 1
            if countExp > limit:
                break

axisX_1 = np.arange(0, N, 1)

traceList = []
for i in range(m):
    traceList.append(go.Scatter(visible=True, x=axisX_1, y=output[0][i], name=colors[i]))
for i in range(1, steps):
    for j in range(m):
        traceList.append(go.Scatter(visible=False, x=axisX_1, y=output[i][j], name=colors[j]))

fig_1 = go.Figure(data=traceList)

steps = []
for i in range(len(output)):
    step = dict(
        label=sliderSteps[i],
        method='restyle',
        args=['visible', [False] * len(fig_1.data)],
    )
    for j in range(m):
        step['args'][1][m * i + j] = True
    steps.append(step)

sliders = [dict(steps=steps, )]
fig_1.layout.sliders = sliders
fig_1.show()

fig_2 = go.Figure()
for i in range(m):
    fig_2.add_trace(go.Scatter(x=sliderSteps, y=quantityWithMaxProb[i], name=colors[i]))
fig_2.show()

fig_3 = go.Figure()
sliderSteps.remove(0)
for i in range(m):
    fig_3.add_trace(go.Scatter(x=sliderSteps, y=quantityBasedOnFrequency[i], name=colors[i]))
fig_3.show()

axisX_2 = np.arange(0, countExp, 1)
fig_4 = go.Figure()
for i in range(m):
    fig_4.add_trace(go.Scatter(x=axisX_2, y=countColors[i], name=colors[i]))
fig_4.show()