from math import comb

import plotly.graph_objs as go
from copy import deepcopy
import random
import numpy

def sum_p_Bernoulli(p, m_left, m_right, n):
    result = 0
    for m in range(m_left, m_right + 1):
        result += (comb(n, m) * (p ** m) * ((1 - p) ** (n - m)))
    return result

def prob_outcomes(symbol_to_prob, columns, rows):
    result = {}
    wild_prob = symbol_to_prob['Wild']
    scatter_prob = symbol_to_prob['Scatter']
    n = columns * rows
    for symbol in symbol_to_prob:
        if symbol == 'Wild' or symbol == "Scatter":
            continue
        p = symbol_to_prob[symbol]

        result[(symbol, 3, 'scatter_lower_2')] = ((wild_prob + p) ** 3) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 0, 1, n - 3)
        result[(symbol, 3, 'scatter_2')] = ((wild_prob + p) ** 3) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 2, 2, n - 3)
        result[(symbol, 3, 'scatter_3')] = ((wild_prob + p) ** 3) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 3, 3, n - 3)
        result[(symbol, 3, 'scatter_4')] = ((wild_prob + p) ** 3) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 4, 4, n - 3)
        result[(symbol, 3, 'scatter_greater_4')] = ((wild_prob + p) ** 3) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 5, n - 3, n - 3)

        result[(symbol, 4, 'scatter_lower_2')] = ((wild_prob + p) ** 4) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 0, 1, n - 4)
        result[(symbol, 4, 'scatter_2')] = ((wild_prob + p) ** 4) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 2, 2, n - 4)
        result[(symbol, 4, 'scatter_3')] = ((wild_prob + p) ** 4) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 3, 3, n - 4)
        result[(symbol, 4, 'scatter_4')] = ((wild_prob + p) ** 4) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 4, 4, n - 4)
        result[(symbol, 4, 'scatter_greater_4')] = ((wild_prob + p) ** 4) * (1 - (wild_prob + p)) * sum_p_Bernoulli(scatter_prob, 5, n - 4, n - 4)

        result[(symbol, 5, 'scatter_lower_2')] = ((wild_prob + p) ** 5) * sum_p_Bernoulli(scatter_prob, 0, 1, n - 5)
        result[(symbol, 5, 'scatter_2')] = ((wild_prob + p) ** 5) * sum_p_Bernoulli(scatter_prob, 2, 2, n - 5)
        result[(symbol, 5, 'scatter_3')] = ((wild_prob + p) ** 5) * sum_p_Bernoulli(scatter_prob, 3, 3, n - 5)
        result[(symbol, 5, 'scatter_4')] = ((wild_prob + p) ** 5) * sum_p_Bernoulli(scatter_prob, 4, 4, n - 5)
        result[(symbol, 5, 'scatter_greater_4')] = ((wild_prob + p) ** 5) * sum_p_Bernoulli(scatter_prob, 5, n - 5, n - 5)

    return result

symbol_to_prob = {'S1': 0.37,
                  'S2': 0.2,
                  'S3': 0.12,
                  'S4': 0.1,
                  'S5': 0.08,
                  'S6': 0.06,
                  'S7': 0.04,
                  'S8': 0.02,
                  'Wild': 0.0075,
                  'Scatter': 0.0025}

symbols_to_prize = {'S1': {3: 3, 4: 20, 5: 45},
                    'S2': {3: 5, 4: 30, 5: 75},
                    'S3': {3: 7, 4: 50, 5: 150},
                    'S4': {3: 9, 4: 60, 5: 250},
                    'S5': {3: 12, 4: 75, 5: 350},
                    'S6': {3: 15, 4: 90, 5: 500},
                    'S7': {3: 20, 4: 120, 5: 750},
                    'S8': {3: 30, 4: 150, 5: 1000}}

scatter_to_x = {'scatter_lower_2': 1, 'scatter_2': 300, 'scatter_3': 600, 'scatter_4': 1200, 'scatter_greater_4': 2400}


columns = 5
rows = 3

probs_outcomes = prob_outcomes(symbol_to_prob, columns, rows)

EV = 0
wager = 1
p_get_prize = 0
for symbol_quantity_scatter in probs_outcomes:
    p_get_prize += probs_outcomes[symbol_quantity_scatter]
    symbol = symbol_quantity_scatter[0]
    quantity = symbol_quantity_scatter[1]
    scatter = symbol_quantity_scatter[2]
    EV += probs_outcomes[symbol_quantity_scatter] * (symbols_to_prize[symbol][quantity] * scatter_to_x[scatter] - wager)
EV += (1 - p_get_prize) * (-wager)

debug = 0


money = 10000
money_list = []

matrix = [['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any']]


def create_matrix(matrix):
    for i in range(len(matrix)):
        column = matrix[i]
        column_len = len(column)
        column_copy = deepcopy(column)
        rnd = random.randint(1, column_len)
        for j in range(column_len):
            column[(rnd + j) % column_len] = column_copy[j]


def get_prize(lines):
    prize = 0
    for line in lines:
        count = 1
        prev = line[0]
        for i in range(1, len(line)):
            next = line[i]
            if next == prev:
                count += 1
            else:
                break
            prev = next
        symbol = line[0]
        if count >= 3 and symbol != 'Scatter':
            prize += symbols_to_prize[symbol][count]
    return prize


money_list.append(money)
while 0 < money < 20000:
    money -= 5
    create_matrix(matrix)

    wild_indexes = []
    for i in range(columns):
        for j in range(rows):
            if matrix[i][j] == 'Wild':
                wild_indexes.append([i, j])

    matrix_variants = []
    symbols_Si = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
    n = len(symbols_to_prize)
    wild_indexes_len = len(wild_indexes)
    for s1 in symbols_Si:
        if wild_indexes_len == 1:
            matrix_variant = deepcopy(matrix)
            matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
            matrix_variants.append(matrix_variant)
        for s2 in symbols_Si:
            if wild_indexes_len < 2:
                break
            if wild_indexes_len == 2:
                matrix_variant = deepcopy(matrix)
                matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
                matrix_variant[wild_indexes[1][0]][wild_indexes[1][1]] = s2
                matrix_variants.append(matrix_variant)
            for s3 in symbols_Si:
                if wild_indexes_len < 3:
                    break
                if wild_indexes_len == 3:
                    matrix_variant = deepcopy(matrix)
                    matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
                    matrix_variant[wild_indexes[1][0]][wild_indexes[1][1]] = s2
                    matrix_variant[wild_indexes[2][0]][wild_indexes[2][1]] = s3
                    matrix_variants.append(matrix_variant)
                for s4 in symbols_Si:
                    if wild_indexes_len < 4:
                        break
                    if wild_indexes_len == 4:
                        matrix_variant = deepcopy(matrix)
                        matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
                        matrix_variant[wild_indexes[1][0]][wild_indexes[1][1]] = s2
                        matrix_variant[wild_indexes[2][0]][wild_indexes[2][1]] = s3
                        matrix_variant[wild_indexes[3][0]][wild_indexes[3][1]] = s4
                        matrix_variants.append(matrix_variant)
                    for s5 in symbols_Si:
                        if wild_indexes_len < 5:
                            break
                        if wild_indexes_len == 5:
                            matrix_variant = deepcopy(matrix)
                            matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
                            matrix_variant[wild_indexes[1][0]][wild_indexes[1][1]] = s2
                            matrix_variant[wild_indexes[2][0]][wild_indexes[2][1]] = s3
                            matrix_variant[wild_indexes[3][0]][wild_indexes[3][1]] = s4
                            matrix_variant[wild_indexes[4][0]][wild_indexes[4][1]] = s5
                            matrix_variants.append(matrix_variant)

    if len(wild_indexes) == 0:
        matrix_variants.append(matrix)

    prize = 0
    matrix_prize = []
    for matrix_variant in matrix_variants:
        line_1 = [matrix_variant[0][0], matrix_variant[1][0], matrix_variant[2][0], matrix_variant[3][0], matrix_variant[4][0]]
        line_2 = [matrix_variant[0][1], matrix_variant[1][1], matrix_variant[2][1], matrix_variant[3][1], matrix_variant[4][1]]
        line_3 = [matrix_variant[0][2], matrix_variant[1][2], matrix_variant[2][2], matrix_variant[3][2], matrix_variant[4][2]]
        line_4 = [matrix_variant[0][0], matrix_variant[1][1], matrix_variant[2][2], matrix_variant[3][1], matrix_variant[4][0]]
        line_5 = [matrix_variant[0][2], matrix_variant[1][1], matrix_variant[2][0], matrix_variant[3][1], matrix_variant[4][2]]
        lines = [line_1, line_2, line_3, line_4, line_5]
        cur_prize = get_prize(lines)

        x = 0
        for i in range(len(matrix_variant)):
            if matrix_variant[i][0] == 'Scatter' or matrix_variant[i][1] == 'Scatter' or matrix_variant[i][2] == 'Scatter':
                x += 1
        if x >= 2:
            cur_prize *= symbols_to_prize['Scatter'][x]

        if x >= 3 and cur_prize != 0:
            debug = 0

        if cur_prize > prize:
            prize = cur_prize
            matrix_prize = matrix_variant

    if prize > 0:
        debug = 0

    money += prize
    money_list.append(money)

x_axis = numpy.arange(0, len(money_list), 1)
y_axis = money_list
figure = go.Figure()
figure.add_trace(go.Scatter(x=x_axis, y=y_axis))
figure.show()