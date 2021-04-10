import plotly.graph_objs as go
import numpy as np
import copy
import re

N = 290
m = 6
limit = 9100

H = [[1 / (N + 1) for i in range(N + 1)] for j in range(m)]
colors = ['Red', 'White', 'Black', 'Green', 'Blue', 'Yellow']

distributions = []
sliderSteps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 40, 50,  100, 200, 300, 400, 500, 1000, 2000, 4000, 9000]
steps = len(sliderSteps)

quantityWithMaxProb = [[] for i in range(m)]

countTakenBallsAll = 0
countTakenBalls = [0] * m
quantityBasedOnFrequency = [[] for i in range(m)]

countHypothesis = [[] for i in range(m)]
minP = 0.000001

with open('Python-sources/balls/task_1_balls.txt') as line:
    countExp = 0

    while True:
        data = re.split(' |, |\n', line.readline())

        if len(data) != 0 and data[0] == '#':
            if len(data) == 6: quantityOfTakenBalls = 2
            elif len(data) == 7: quantityOfTakenBalls = 3
            else: break

            for i in range(m):
                count = 0
                for j in range(N + 1):
                    if H[i][j] > minP:
                        count += 1
                countHypothesis[i].append(count)

            if sliderSteps.__contains__(countExp):
                distributions.append(copy.deepcopy(H))

            A_I_Hj = [[0 for i in range(N + 1)] for j in range(m)]
            nA_I_Hj = [[0 for i in range(N + 1)] for j in range(m)]
            Hj_I_A = [[0 for i in range(N + 1)] for j in range(m)]
            Hj_I_nA = [[0 for i in range(N + 1)] for j in range(m)]

            ki = [0] * m
            for i in range(len(data) - quantityOfTakenBalls - 1, len(data) - 1):
                ki[colors.index(data[i])] += 1

                countTakenBalls[colors.index(data[i])] += 1
            countTakenBallsAll += quantityOfTakenBalls
            for i in range(m):
                quantityBasedOnFrequency[i].append((countTakenBalls[i] / countTakenBallsAll) * N)

                quantityWithMaxProb[i].append(H[i].index(max(H[i])))

            for i in range(m):
                if ki[i] > 0:
                    for j in range(N + 1): A_I_Hj[i][j] += (j / N) ** ki[i]
                else:
                    for j in range(N + 1): nA_I_Hj[i][j] += (N - j) / N

            for i in range(m):
                if ki[i] > 0:
                    E = 0
                    for j in range(N + 1): E += H[i][j] * A_I_Hj[i][j]
                    for j in range(N + 1): Hj_I_A[i][j] += H[i][j] * A_I_Hj[i][j] / E
                else:
                    E = 0
                    for j in range(N + 1): E += H[i][j] * nA_I_Hj[i][j]
                    for j in range(N + 1): Hj_I_nA[i][j] += H[i][j] * nA_I_Hj[i][j] / E

            for i in range(m):
                if ki[i] > 0:
                    for j in range(N + 1): H[i][j] = Hj_I_A[i][j]
                else:
                    for j in range(N + 1): H[i][j] = Hj_I_nA[i][j]

            countExp += 1
            if countExp > limit: break

axisFrom0ToN = np.arange(0, N, 1)
traceList = []
for i in range(m):
    traceList.append(go.Scatter(visible=True, x=axisFrom0ToN, y=distributions[0][i], name=colors[i]))
for i in range(1, steps):
    for j in range(m):
        traceList.append(go.Scatter(visible=False, x=axisFrom0ToN, y=distributions[i][j], name=colors[j]))
figDistributions = go.Figure(data=traceList)
steps = []
for i in range(len(distributions)):
    step = dict(label=sliderSteps[i], method='restyle', args=['visible', [False] * len(figDistributions.data)])
    for j in range(m):
        step['args'][1][m * i + j] = True
    steps.append(step)
sliders = [dict(steps=steps)]
figDistributions.layout.sliders = sliders
figDistributions.show()

axisFrom0ToCountExp = np.arange(0, countExp, 1)
figQuantityWithMaxProb = go.Figure()
figQuantityBasedOnFrequency = go.Figure()
figCountHypothesis = go.Figure()
for i in range(m):
    figQuantityWithMaxProb.add_trace(go.Scatter(x=axisFrom0ToCountExp, y=quantityWithMaxProb[i], name=colors[i]))
    figQuantityBasedOnFrequency.add_trace(go.Scatter(x=np.arange(1, countExp, 1), y=quantityBasedOnFrequency[i], name=colors[i]))
    figCountHypothesis.add_trace(go.Scatter(x=axisFrom0ToCountExp, y=countHypothesis[i], name=colors[i]))
figQuantityWithMaxProb.show()
figQuantityBasedOnFrequency.show()
figCountHypothesis.show()