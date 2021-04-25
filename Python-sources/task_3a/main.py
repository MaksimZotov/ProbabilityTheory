import plotly.graph_objs as go
from scipy.special import comb
import numpy as np
import copy
import random
import re
import math


def k(x):
    return math.exp(- x * x / 2) / math.sqrt(2 * math.pi)


def p_KDE(x):
    sigma = 0
    for i in range(N):
        sigma += k((x - listOfValuesFloat[i]) / h_opt)
    return sigma / (N * h_opt)


parts = 10

N = 0
with open('Python-sources/task_3a/Task_3a.txt') as line:
    N = int(re.split(' |, |\n', line.readline())[2])
    listOfValuesStr = re.split(' |, |\n', line.readline())
    listOfValuesFloat = []
    for i in range(N):
        listOfValuesFloat.append(float(listOfValuesStr[i]))
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

    # Определение мат. ожидания
    M = listOfValuesFloat[int(N / 2)]

    # Поиск дисперсии
    sigma = 0
    for i in range(N):
        sigma += (M - listOfValuesFloat[i]) ** 2
    D = sigma / N

    # Функция распределения
    F = []
    x_for_F = []
    for i in range(N):
        x_for_F.append(listOfValuesFloat[i])
        x_for_F.append(listOfValuesFloat[i])
        F.append(i / N)
        F.append((i + 1) / N)

    # Функция плотности распределения
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
                f.append(curCount / N)
            curCount = 0
            curMax += interval
    if curCount > 0:
        for j in range(curCount):
            f.append(curCount / N)

    # Определение h_opt
    h_opt = 1.06 * math.sqrt(D) * (N ** (- 1 / 5))

    # Ядерная оценка плотности
    f_KDE = []
    for value in listOfValuesFloat:
        f_KDE.append(p_KDE(value))

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x_for_F, y=F))
fig1.show()

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x_for_f, y=f))
fig2.show()

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=listOfValuesFloat, y=f_KDE))
fig3.show()
