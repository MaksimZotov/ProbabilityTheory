import plotly.graph_objs as go
from scipy.special import comb
import numpy as np
import copy
import re

N = 290
m = 6
limit = 9100

startPComb = 1 / comb(N + m - 1, m - 1)

# вычислены заранее (см. ниже)
bestCombinations = {(10, 50, 20, 70, 80, 60): startPComb,
                    (10, 50, 20, 80, 70, 60): startPComb,
                    (10, 60, 20, 60, 80, 60): startPComb,
                    (10, 60, 20, 70, 70, 60): startPComb,
                    (10, 60, 20, 70, 80, 50): startPComb,
                    (10, 60, 20, 80, 60, 60): startPComb,
                    (10, 60, 20, 80, 70, 50): startPComb,
                    (10, 70, 20, 60, 70, 60): startPComb,
                    (10, 70, 20, 70, 60, 60): startPComb,
                    (10, 70, 20, 70, 70, 50): startPComb}

combinationsToShow_n = 10
combinationsToShow_y = {(10, 50, 20, 70, 80, 60): [startPComb],
                        (10, 50, 20, 80, 70, 60): [startPComb],
                        (10, 60, 20, 60, 80, 60): [startPComb],
                        (10, 60, 20, 70, 70, 60): [startPComb],
                        (10, 60, 20, 70, 80, 50): [startPComb],
                        (10, 60, 20, 80, 60, 60): [startPComb],
                        (10, 60, 20, 80, 70, 50): [startPComb],
                        (10, 70, 20, 60, 70, 60): [startPComb],
                        (10, 70, 20, 70, 60, 60): [startPComb],
                        (10, 70, 20, 70, 70, 50): [startPComb]}
#combinationsToShow = []

combForPerformance = {}
for i in range(N + 1):
    for j in range(4):
        combForPerformance[(i, j)] = comb(i, j)

minPComb = startPComb / 100
c_2_from_N = comb(N, 2)
c_3_from_N = comb(N, 3)
maxCombinations = []
combinations = {}
countHypothesisComb = []
denominator = 29
for i0 in range(denominator + 1):
    for i1 in range(denominator - i0 + 1):
        sum1 = i0 + i1
        for i2 in range(denominator - sum1 + 1):
            sum2 = sum1 + i2
            for i3 in range(denominator - sum2 + 1):
                sum3 = sum2 + i3
                for i4 in range(denominator - sum3 + 1):
                    sum4 = sum3 + i4
                    i5 = denominator - sum4
                    if i0 + i1 + i2 + i3 + i4 + i5 == denominator:
                        combinations[round((i0 / denominator) * N),
                                     round((i1 / denominator) * N),
                                     round((i2 / denominator) * N),
                                     round((i3 / denominator) * N),
                                     round((i4 / denominator) * N),
                                     round((i5 / denominator) * N)] = startPComb

H = [[1 / (N + 1) for i in range(N + 1)] for j in range(m)]
colors = ['Red', 'White', 'Black', 'Green', 'Blue', 'Yellow']

distributions = []
sliderSteps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 2000, 4000, 9000]
steps = len(sliderSteps)

quantityWithMaxProb = [[] for i in range(m)]

countTakenBallsAll = 0
countTakenBalls = [0] * m
quantityBasedOnFrequency = [[] for i in range(m)]

countHypothesisEachColor = [[] for i in range(m)]
minPEachColor = 0.000001

with open('Python-sources/balls/task_1_balls.txt') as line:
    countExp = 0

    while True:
        data = re.split(' |, |\n', line.readline())

        if len(data) != 0 and data[0] == '#':
            if len(data) == 6:
                quantityOfTakenBalls = 2
                denominator = c_2_from_N
            elif len(data) == 7:
                quantityOfTakenBalls = 3
                denominator = c_3_from_N
            else:
                break

            for i in range(m):
                count = 0
                for j in range(N + 1):
                    if H[i][j] > minPEachColor:
                        count += 1
                countHypothesisEachColor[i].append(count)

            if sliderSteps.__contains__(countExp):
                distributions.append(copy.deepcopy(H))

            A_I_H = [[0.0 for i in range(N + 1)] for j in range(m)]
            H_I_A = [[0.0 for i in range(N + 1)] for j in range(m)]

            localCountTakenBalls = [0] * m
            for i in range(len(data) - quantityOfTakenBalls - 1, len(data) - 1):
                localCountTakenBalls[colors.index(data[i])] += 1

                countTakenBalls[colors.index(data[i])] += 1
            countTakenBallsAll += quantityOfTakenBalls
            for i in range(m):
                quantityBasedOnFrequency[i].append((countTakenBalls[i] / countTakenBallsAll) * N)

                quantityWithMaxProb[i].append(H[i].index(max(H[i])))

            countHypothesisComb.append(len(combinations))
            combinationsCopy_A_I_H = copy.deepcopy(combinations)
            sumCombinationsCopy_A_I_H = 0
            for combination in combinationsCopy_A_I_H:
                if combinations[combination] < minPComb:
                    combinations.pop(combination)

                    if len(combinations) == combinationsToShow_n:
                        for item in combinations:
                            print(item) # !!!!!!!!!!!!!----------------------------------------------------------------------> bestCombinations

                    continue

                combinationsCopy_A_I_H[combination] = 1
                for i in range(m):
                    combinationsCopy_A_I_H[combination] *= comb(combination[i], localCountTakenBalls[i])
                combinationsCopy_A_I_H[combination] /= denominator
                sumCombinationsCopy_A_I_H += combinations[combination] * combinationsCopy_A_I_H[combination]
            maxP = 0
            maxComb = (0, 0, 0, 0, 0, 0)
            for combination in combinations:
                combinations[combination] = combinations[combination] * combinationsCopy_A_I_H[combination] / sumCombinationsCopy_A_I_H
                if combinations[combination] > maxP:
                    maxP = combinations[combination]
                    maxComb = combination
            maxCombinations.append((maxComb, maxP))

            bestCombinationsCopy_A_I_H = copy.deepcopy(bestCombinations)
            sumBestCombinationsCopy_A_I_H = 0
            for combination in bestCombinationsCopy_A_I_H:
                bestCombinationsCopy_A_I_H[combination] = 1
                for i in range(m):
                    bestCombinationsCopy_A_I_H[combination] *= comb(combination[i], localCountTakenBalls[i])
                bestCombinationsCopy_A_I_H[combination] /= denominator
                sumBestCombinationsCopy_A_I_H += bestCombinations[combination] * bestCombinationsCopy_A_I_H[combination]
            for combination in bestCombinations:
                bestCombinations[combination] = bestCombinations[combination] * bestCombinationsCopy_A_I_H[combination] / sumBestCombinationsCopy_A_I_H

            for key in bestCombinations:
                combinationsToShow_y[key].append(bestCombinations[key])

            for i in range(m):
                for j in range(N + 1):
                    if j < localCountTakenBalls[i]:
                        A_I_H[i][j] = 0
                    else:
                        c1 = combForPerformance[(j, localCountTakenBalls[i])]
                        c2 = combForPerformance[(N - j, quantityOfTakenBalls - localCountTakenBalls[i])]
                        A_I_H[i][j] = c1 * c2 / denominator

            for i in range(m):
                E = 0
                for j in range(N + 1): E += H[i][j] * A_I_H[i][j]
                for j in range(N + 1): H_I_A[i][j] += H[i][j] * A_I_H[i][j] / E

            for i in range(m):
                 for j in range(N + 1):
                     H[i][j] = H_I_A[i][j]

            countExp += 1
            if countExp > limit:
                break

combEachColor = [[] for i in range(m)]
for i in range(m):
    for combination in maxCombinations:
        combEachColor[i].append(combination[0][i])

axisFrom0ToN = np.arange(0, N, 1)
axisFrom0ToCountExp = np.arange(0, countExp, 1)

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

figDistributionsComb = go.Figure()
figCountHypothesisComp = go.Figure()
figQuantityWithMaxProb = go.Figure()
figQuantityBasedOnFrequency = go.Figure()
figCountHypothesis = go.Figure()
figCountHypothesisComp.add_trace(go.Scatter(x=axisFrom0ToCountExp, y=countHypothesisComb))
for i in range(m):
    figDistributionsComb.add_trace(go.Scatter(x=axisFrom0ToCountExp, y=combEachColor[i], name=colors[i]))
    figQuantityWithMaxProb.add_trace(go.Scatter(x=axisFrom0ToCountExp, y=quantityWithMaxProb[i], name=colors[i]))
    figQuantityBasedOnFrequency.add_trace(go.Scatter(x=np.arange(1, countExp, 1), y=quantityBasedOnFrequency[i], name=colors[i]))
    figCountHypothesis.add_trace(go.Scatter(x=axisFrom0ToCountExp, y=countHypothesisEachColor[i], name=colors[i]))
figDistributionsComb.show()
figCountHypothesisComp.show()
figQuantityWithMaxProb.show()
figQuantityBasedOnFrequency.show()
figCountHypothesis.show()

figCombToShow = go.Figure()
axisXForCombToShow = np.arange(0, countExp)
for key in combinationsToShow_y:
    figCombToShow.add_trace(go.Scatter(x=axisXForCombToShow, y=combinationsToShow_y[key], name=str(key)))
figCombToShow.show()