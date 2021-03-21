import plotly.graph_objs as go
import numpy as np
import copy
import re


def c_m_n(m, n):
    if m == 0: return 1
    denominator = 1
    numeratorLeft = 1
    numeratorRight = 1
    for i in range(2, n): denominator *= i
    for i in range(2, m): numeratorLeft *= i
    for i in range(2, n - m): numeratorRight *= i
    return denominator / (numeratorLeft * numeratorRight)


n_boxes = 6
m = 5
d = 4
p_change_box = 0.1
nExp = 1000

limit_1_c = 0.0000001
colorsCount_2_a = {'Red': 0, 'White': 0, 'Black': 0, 'Green': 0, 'Blue': 0}
colorsCountList_2_с = {'Red': [], 'White': [], 'Black': [], 'Green': [], 'Blue': []}
for color in colorsCountList_2_с:
    colorsCountList_2_с[color] = [0] * (nExp + 1)

colorToNumber = {'Red': 0, 'White': 1, 'Black': 2, 'Green': 3, 'Blue': 4}
colorsRGB = {'Red': '#FF0000', 'White': '#FFFFFF', 'Black': '#000000', 'Green': '#00FF00', 'Blue': '#0000FF'}

boxes = [[210, 47, 56, 57, 8, 42],
         [200, 26, 45, 43, 47, 39],
         [250, 84, 67, 53, 40, 6],
         [270, 71, 27, 85, 53, 34],
         [220, 43, 36, 31, 46, 64],
         [250, 83, 22, 56, 23, 66]]

sumBalls = 0
for i in range(n_boxes):
    sumBalls += boxes[i][0]

numerator = c_m_n(d, sumBalls)

HSlashAList = [[]] * n_boxes
for i in range(n_boxes):
    HSlashAList[i] = [0] * (nExp + 1)
    HSlashAList[i][0] = 1 / n_boxes

with open('Python-sources/ball_boxes/ball_boxes.txt') as line:
    countExp = 0
    H = [1 / n_boxes] * n_boxes

    while True:
        data = re.split(' |, |\n', line.readline())

        if len(data) == d + 4 and data[0] == '#':
            localBoxes = copy.deepcopy(boxes)
            colorBalls = [data[3], data[4], data[5], data[6]]

            ballsQuantity = [0] * m
            for colorBall in colorBalls:
                ballsQuantity[colorToNumber[colorBall]] += 1
                colorsCount_2_a[colorBall] += 1

            for colorBall in colorsCount_2_a.keys():
                colorsCountList_2_с[colorBall][countExp + 1] = colorsCount_2_a[colorBall] / (d * (countExp + 1))

            ASlashH = [1] * n_boxes
            for i in range(n_boxes):
                for j in range(m):
                    ASlashH[i] *= c_m_n(ballsQuantity[j], boxes[i][j + 1])
                ASlashH[i] /= numerator

            HSlashA = [0] * n_boxes
            for i in range(n_boxes):
                for j in range(n_boxes):
                    HSlashA[i] += H[j] * ASlashH[j]
                HSlashA[i] = H[i] * ASlashH[i] / HSlashA[i]
                HSlashAList[i][countExp + 1] = HSlashA[i]

            for i in range(n_boxes):
                H[i] = HSlashA[i] * (1 - p_change_box)

            countExp += 1
            if countExp == nExp:
                break

k = np.arange(0, nExp, 1)


fig_1_a_b = go.Figure()
for i in range(n_boxes):
    fig_1_a_b.add_trace(go.Scatter(x=k, y=HSlashAList[i], name=str(i + 1)))
fig_1_a_b.show()

count = [0] * (nExp + 1)
for i in range(n_boxes):
    for j in range(nExp + 1):
        if HSlashAList[i][j] > limit_1_c:
            count[j] += 1
fig_1_c = go.Figure()
fig_1_c.add_trace(go.Scatter(x=k, y=count, name='hypothesis'))
fig_1_c.show()

print('2.a:')
for item in colorsCount_2_a:
    colorsCount_2_a[item] /= (nExp * d)
    print(item, '=\t', colorsCount_2_a[item])

print('\n\n2.b:\n')
for i in range(n_boxes):
    print('box ', i + 1, ':')
    DIF = 0
    for color in colorToNumber.keys():
        tp = boxes[i][colorToNumber[color] + 1] / boxes[i][0]
        print(color, '=\t', tp, '\tdif =', abs(tp - colorsCount_2_a[color]))
        DIF += abs(tp - colorsCount_2_a[color])
    print('DIF =\t', DIF, '\n')

fig_2_c = go.Figure(layout=go.Layout(paper_bgcolor='#D3D3D3', plot_bgcolor='#708090'))
for color in colorsCountList_2_с.keys():
    fig_2_c.add_trace(go.Scatter(x=k, y=colorsCountList_2_с[color], name=color, line=dict(color=colorsRGB[color])))
fig_2_c.show()
