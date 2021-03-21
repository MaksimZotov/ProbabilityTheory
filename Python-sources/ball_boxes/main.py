import plotly.graph_objs as go
import numpy as np
import copy
import re

n_boxes = 6
m = 5
d = 4
nExp = 50

boxes = [{'Total': 210, 'Red': 47, 'White': 56, 'Black': 57, 'Green': 8, 'Blue': 42},
         {'Total': 200, 'Red': 26, 'White': 45, 'Black': 43, 'Green': 47, 'Blue': 39},
         {'Total': 250, 'Red': 84, 'White': 67, 'Black': 53, 'Green': 40, 'Blue': 6},
         {'Total': 270, 'Red': 71, 'White': 27, 'Black': 85, 'Green': 53, 'Blue': 34},
         {'Total': 220, 'Red': 43, 'White': 36, 'Black': 31, 'Green': 46, 'Blue': 64},
         {'Total': 250, 'Red': 83, 'White': 22, 'Black': 56, 'Green': 23, 'Blue': 66}]

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

            ASlashH = [1] * n_boxes
            for i in range(n_boxes):
                for colorBall in colorBalls:
                    ASlashH[i] *= localBoxes[i][colorBall] / localBoxes[i]['Total']
                    localBoxes[i][colorBall] -= 1
                    localBoxes[i]['Total'] -= 1

            HSlashA = [0] * n_boxes
            for i in range(n_boxes):
                for j in range(n_boxes):
                    HSlashA[i] += H[j] * ASlashH[j]
                HSlashA[i] = H[i] * ASlashH[i] / HSlashA[i]
                HSlashAList[i][countExp + 1] = HSlashA[i]

            for i in range(n_boxes):
                H[i] = HSlashA[i]

            countExp += 1
            if countExp == nExp:
                break

k = np.arange(0, nExp, 1)

fig = go.Figure()
for i in range(n_boxes):
    fig.add_trace(go.Scatter(x=k, y=HSlashAList[i], name=str(i + 1)))
fig.show()
