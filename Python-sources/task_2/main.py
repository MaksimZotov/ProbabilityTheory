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

symbol_to_prob = {'S1': 0.18,
                  'S2': 0.16,
                  'S3': 0.15,
                  'S4': 0.13,
                  'S5': 0.11,
                  'S6': 0.09,
                  'S7': 0.07,
                  'S8': 0.05,
                  'Wild': 0.04,
                  'Scatter': 0.02}

symbols_to_prize = {'S1': {3: 3, 4: 15, 5: 45},
                    'S2': {3: 5, 4: 30, 5: 75},
                    'S3': {3: 7, 4: 50, 5: 150},
                    'S4': {3: 9, 4: 60, 5: 250},
                    'S5': {3: 12, 4: 75, 5: 350},
                    'S6': {3: 15, 4: 90, 5: 500},
                    'S7': {3: 20, 4: 120, 5: 750},
                    'S8': {3: 30, 4: 150, 5: 1000}}

scatter_to_x = {'scatter_lower_2': 1, 'scatter_2': 15, 'scatter_3': 40, 'scatter_4': 75, 'scatter_greater_4': 100}


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

PRIZE_EXPECTED = EV


money = 10000
money_list = []

matrix = [['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any']]


def create_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sigma = 0
            rnd = random.random()
            for symbol in symbol_to_prob:
                sigma += symbol_to_prob[symbol]
                if sigma >= rnd:
                    matrix[i][j] = symbol
                    break


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

def get_prize_from_line(line):
    prize = 0
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

def create_matrix_variants(matrix, matrix_variants, wild_indexes, symbols_si, si_iter):
    if len(wild_indexes) > len(si_iter):
        for symbol in symbols_si:
            si_iter_cur = deepcopy(si_iter)
            si_iter_cur.append(symbol)
            create_matrix_variants(matrix, matrix_variants, wild_indexes, symbols_si, si_iter_cur)
    else:
        matrix_variant = deepcopy(matrix)
        for s in range(len(si_iter)):
            matrix_variant[wild_indexes[s][0]][wild_indexes[s][1]] = si_iter[s]
        matrix_variants.append(matrix_variant)

money_list.append(money)
prize_list_1 = []
prize_list_2 = []
prize_list_3 = []
prize_list_4 = []
prize_list_5 = []
for i in range(100000):
    create_matrix(matrix)

    wild_indexes = []
    for i in range(columns):
        for j in range(rows):
            if matrix[i][j] == 'Wild':
                wild_indexes.append([i, j])

    matrix_variants = []
    symbols_si = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']

    create_matrix_variants(matrix, matrix_variants, wild_indexes, symbols_si, [])

    prize_1 = 0
    prize_2 = 0
    prize_3 = 0
    prize_4 = 0
    prize_5 = 0
    for matrix_variant in matrix_variants:
        line_1 = [matrix_variant[0][0], matrix_variant[1][0], matrix_variant[2][0], matrix_variant[3][0], matrix_variant[4][0]]
        line_2 = [matrix_variant[0][1], matrix_variant[1][1], matrix_variant[2][1], matrix_variant[3][1], matrix_variant[4][1]]
        line_3 = [matrix_variant[0][2], matrix_variant[1][2], matrix_variant[2][2], matrix_variant[3][2], matrix_variant[4][2]]
        line_4 = [matrix_variant[0][0], matrix_variant[1][1], matrix_variant[2][2], matrix_variant[3][1], matrix_variant[4][0]]
        line_5 = [matrix_variant[0][2], matrix_variant[1][1], matrix_variant[2][0], matrix_variant[3][1], matrix_variant[4][2]]

        cur_prize_1 = get_prize_from_line(line_1)
        cur_prize_2 = get_prize_from_line(line_2)
        cur_prize_3 = get_prize_from_line(line_3)
        cur_prize_4 = get_prize_from_line(line_4)
        cur_prize_5 = get_prize_from_line(line_5)

        x = 0
        for i in range(len(matrix_variant)):
            for j in range(len(matrix_variant[i])):
                if matrix_variant[i][j] == 'Scatter':
                    x += 1
        if x >= 2:
            if x == 2:
                cur_prize_1 *= scatter_to_x['scatter_2']
                cur_prize_2 *= scatter_to_x['scatter_2']
                cur_prize_3 *= scatter_to_x['scatter_2']
                cur_prize_4 *= scatter_to_x['scatter_2']
                cur_prize_5 *= scatter_to_x['scatter_2']
            elif x == 3:
                cur_prize_1 *= scatter_to_x['scatter_3']
                cur_prize_2 *= scatter_to_x['scatter_3']
                cur_prize_3 *= scatter_to_x['scatter_3']
                cur_prize_4 *= scatter_to_x['scatter_3']
                cur_prize_5 *= scatter_to_x['scatter_3']
            elif x == 4:
                cur_prize_1 *= scatter_to_x['scatter_4']
                cur_prize_2 *= scatter_to_x['scatter_4']
                cur_prize_3 *= scatter_to_x['scatter_4']
                cur_prize_4 *= scatter_to_x['scatter_4']
                cur_prize_5 *= scatter_to_x['scatter_4']
            elif x == 5:
                cur_prize_1 *= scatter_to_x['scatter_greater_4']
                cur_prize_2 *= scatter_to_x['scatter_greater_4']
                cur_prize_3 *= scatter_to_x['scatter_greater_4']
                cur_prize_4 *= scatter_to_x['scatter_greater_4']
                cur_prize_5 *= scatter_to_x['scatter_greater_4']

        if cur_prize_1 > prize_1: prize_1 = cur_prize_1
        if cur_prize_2 > prize_2: prize_2 = cur_prize_2
        if cur_prize_3 > prize_3: prize_3 = cur_prize_3
        if cur_prize_4 > prize_4: prize_4 = cur_prize_4
        if cur_prize_5 > prize_5: prize_5 = cur_prize_5

    prize_list_1.append(prize_1 - 1)
    prize_list_2.append(prize_2 - 1)
    prize_list_3.append(prize_3 - 1)
    prize_list_4.append(prize_4 - 1)
    prize_list_5.append(prize_5 - 1)

    money_list.append(money)

PRIZE_1_ACTUAL = sum(prize_list_1) / len(prize_list_1)
PRIZE_2_ACTUAL = sum(prize_list_2) / len(prize_list_2)
PRIZE_3_ACTUAL = sum(prize_list_3) / len(prize_list_3)
PRIZE_4_ACTUAL = sum(prize_list_4) / len(prize_list_4)
PRIZE_5_ACTUAL = sum(prize_list_5) / len(prize_list_5)

x_axis = numpy.arange(0, len(money_list), 1)
y_axis = money_list
figure = go.Figure()
figure.add_trace(go.Scatter(x=x_axis, y=y_axis))
figure.show()