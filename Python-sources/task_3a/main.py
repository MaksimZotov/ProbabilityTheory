import plotly.graph_objs as go
from scipy.special import comb
import numpy as np
import copy
import random
import re

parts = 10

N = 0
with open('Python-sources/task_3a/Task_3a.txt') as line:
    N = int(re.split(' |, |\n', line.readline())[2])
    listOfValuesStr = re.split(' |, |\n', line.readline())
    listOfValuesFloat = []
    for i in range(N):
        listOfValuesFloat.append(float(listOfValuesStr[i]))
    debug = 0
    random.shuffle(listOfValuesFloat)
    listsParts = []
    part = 0
    count = 0
    for i in range(N):
        if count == 0:
            listsParts.append([])
        listsParts[part].append(listOfValuesFloat[i])
        count += 1
        if count == N / parts:
            part += 1
            count = 0
    listOfValuesFloat.sort()

    F = []
    x_for_F = []
    for i in range(N):
        x_for_F.append(listOfValuesFloat[i])
        x_for_F.append(listOfValuesFloat[i])
        F.append(i / N)
        F.append((i + 1) / N)

    m = N / 300
    interval = (max(listOfValuesFloat) - min(listOfValuesFloat)) / m
    index = 0
    f = []
    x_for_f = []
    curCount = 0
    curMax = interval
    for i in range(N):
        x_for_f.append(listOfValuesFloat[i])
        curCount += 1
        if listOfValuesFloat[i] > curMax:
            for j in range(curCount):
                f.append(curCount)
            curCount = 0
            curMax += interval
    if curCount > 0:
        for j in range(curCount):
            f.append(curCount)

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x_for_F, y=F))
fig1.show()

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x_for_f, y=f))
fig2.show()

debug = 0
