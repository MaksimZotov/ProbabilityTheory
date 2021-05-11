import math
from math import comb
import plotly.graph_objs as go
import random

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

lines = ['line_1', 'line_2', 'line_3', 'line_4', 'line_5']


columns = 5
rows = 3
wager = 1

probs_outcomes = prob_outcomes(symbol_to_prob, columns, rows)

EV = 0

M = 0
MODA = 0
MID = 0
MODA_P = -1.0
MAX_PRIZE = -1
MIN_PRIZE = 0

p_get_prize = 0
axis_x = []
axis_y = []
for symbol_quantity_scatter in probs_outcomes:
    symbol = symbol_quantity_scatter[0]
    quantity = symbol_quantity_scatter[1]
    scatter = symbol_quantity_scatter[2]
    prize = symbols_to_prize[symbol][quantity] * scatter_to_x[scatter] * wager

    net_pay = wager - prize
    pi = probs_outcomes[symbol_quantity_scatter]
    EV += net_pay * pi
    p_get_prize += pi

    M += pi * prize

    if MODA_P < pi:
        MODA_P = pi
        MODA = prize
    if MAX_PRIZE < prize:
        MAX_PRIZE = prize

    axis_x.append(prize)
    axis_y.append(pi)

axis_x = [0] + sorted(axis_x)
axis_y = [1 - p_get_prize] + sorted(axis_y, reverse=True)
go.Figure(go.Scatter(x=axis_x, y=axis_y)).show()
EV += wager * (1 - p_get_prize)
M += 0 * (1 - p_get_prize)
MID = (MAX_PRIZE + MIN_PRIZE) / 2

axis_x_F = [0]
axis_y_F = [0]
for n in range(len(axis_x)):
    axis_y_F.append(axis_y_F[n] + axis_y[n])
    axis_x_F.append(axis_x[n])
go.Figure(go.Scatter(x=axis_x_F, y=axis_y_F)).show()

HA = EV * 100
RTP = 100 - HA

VAR = 0
for symbol_quantity_scatter in probs_outcomes:
    symbol = symbol_quantity_scatter[0]
    quantity = symbol_quantity_scatter[1]
    scatter = symbol_quantity_scatter[2]
    net_pay = wager - symbols_to_prize[symbol][quantity] * scatter_to_x[scatter] * wager
    pi = probs_outcomes[symbol_quantity_scatter]
    VAR += ((net_pay - EV) ** 2) * pi
VAR += ((wager - EV) ** 2) * (1 - p_get_prize)

SD = math.sqrt(VAR)
V_I = 1.96 * SD

theoretical_payback_x = []
theoretical_payback_above_y = []
theoretical_payback_below_y = []
theoretical_payback_EV_y = []
for n in range(1, 501):
    V_I_div_sqrt_n = V_I / math.sqrt(n)
    theoretical_payback_x.append(n)
    theoretical_payback_above_y.append(EV + V_I_div_sqrt_n)
    theoretical_payback_below_y.append(EV - V_I_div_sqrt_n)
    theoretical_payback_EV_y.append(EV)

figure = go.Figure()
figure.add_trace(go.Scatter(x=theoretical_payback_x, y=theoretical_payback_above_y))
figure.add_trace(go.Scatter(x=theoretical_payback_x, y=theoretical_payback_below_y))
figure.add_trace(go.Scatter(x=theoretical_payback_x, y=theoretical_payback_EV_y))
figure.show()

p_get_prize_list_y = [p_get_prize]
p_get_prize_list_x = [1]
p_get_prize_list_y_F = [0, p_get_prize]
p_get_prize_list_x_F = [0, 1]
for n in range(2, 501):
    p_get_prize_list_y.append((1 - p_get_prize) ** (n - 1) * p_get_prize)
    p_get_prize_list_x.append(n)
    p_get_prize_list_y_F.append(p_get_prize_list_y_F[n - 1] + (1 - p_get_prize) ** (n - 1) * p_get_prize)
    p_get_prize_list_x_F.append(n)
go.Figure(go.Scatter(x=p_get_prize_list_x, y=p_get_prize_list_y)).show()
go.Figure(go.Scatter(x=p_get_prize_list_x_F, y=p_get_prize_list_y_F)).show()

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

def get_prize_from_line(line):
    prize = 0
    count = 0
    wild_index = 0
    symbol = 'any'
    if line[0] == 'Wild':
        for i in range(len(line)):
            if line[i] == 'Wild':
                wild_index = i
                count += 1
            else:
                break
        if count == 5:
            return symbols_to_prize['S8'][count]
        else:
            next_after_wild = line[wild_index + 1]
            if next_after_wild == 'Scatter':
                if count >= 3:
                    return symbols_to_prize['S8'][count]
                else:
                    return 0
        symbol = line[wild_index + 1]
    else:
        count = 1
        wild_index = 0
        symbol = line[0]
    prev = symbol
    for i in range(wild_index + 1, len(line)):
        next = line[i]
        if prev == next or next == 'Wild':
            count += 1
        else:
            break
    if count >= 3 and symbol != 'Scatter':
        return symbols_to_prize[symbol][count]
    return prize


symbols_si = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']

matrix = [['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any'],
          ['any', 'any', 'any']]


p_win_dict = {'line_1': {}, 'line_2': {}, 'line_3': {}, 'line_4': {}, 'line_5': {}}
line_n = [1, 1, 1, 1, 1]
EV_list = [[], [], [], [], []]

N = 100000
p_get_prize_n = [0, 0, 0, 0, 0]
for i in range(N):
    create_matrix(matrix)
    line_1 = [matrix[0][0], matrix[1][0], matrix[2][0], matrix[3][0], matrix[4][0]]
    line_2 = [matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1], matrix[4][1]]
    line_3 = [matrix[0][2], matrix[1][2], matrix[2][2], matrix[3][2], matrix[4][2]]
    line_4 = [matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][1], matrix[4][0]]
    line_5 = [matrix[0][2], matrix[1][1], matrix[2][0], matrix[3][1], matrix[4][2]]
    prize_n = [get_prize_from_line(line_1), get_prize_from_line(line_2), get_prize_from_line(line_3), get_prize_from_line(line_4), get_prize_from_line(line_5)]

    x = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'Scatter':
                x += 1

    if x == 2:
        for n in range(len(prize_n)): prize_n[n] *= scatter_to_x['scatter_2']
    elif x == 3:
        for n in range(len(prize_n)): prize_n[n] *= scatter_to_x['scatter_3']
    elif x == 4:
        for n in range(len(prize_n)): prize_n[n] *= scatter_to_x['scatter_4']
    elif x == 5:
        for n in range(len(prize_n)): prize_n[n] *= scatter_to_x['scatter_greater_4']

    for i in range(len(p_get_prize_n)):
        if prize_n[i] > 0:
            p_get_prize_n[i] += 1
            if p_win_dict[lines[i]].__contains__(line_n[i]): p_win_dict[lines[i]][line_n[i]] += 1
            else: p_win_dict[lines[i]][line_n[i]] = 1
            line_n[i] = 1
        else:
            line_n[i] += 1

    for i in range(len(EV_list)):
        EV_list[i].append(wager - prize_n[i])

for i in range(len(p_get_prize_n)):
    p_get_prize_n[i] = p_get_prize_n[i] / N

p_win_dict_new_keys = {'line_1': {}, 'line_2': {}, 'line_3': {}, 'line_4': {}, 'line_5': {}}
for line_p_win in p_win_dict:
    p_win_dict_new_keys[line_p_win] = sorted(p_win_dict[line_p_win])

p_win_dict_new_keys_and_values = {'line_1': {}, 'line_2': {}, 'line_3': {}, 'line_4': {}, 'line_5': {}}
for line in p_win_dict_new_keys:
    for n in p_win_dict_new_keys[line]:
        p_win_dict_new_keys_and_values[line][n] = p_win_dict[line][n]

acc = {'line_1': 0, 'line_2': 0, 'line_3': 0, 'line_4': 0, 'line_5': 0}
for line in acc:
    for n in p_win_dict_new_keys_and_values[line]:
        acc[line] += p_win_dict_new_keys_and_values[line][n]

axis_x = {'line_1': [], 'line_2': [], 'line_3': [], 'line_4': [], 'line_5': []}
axis_y = {'line_1': [], 'line_2': [], 'line_3': [], 'line_4': [], 'line_5': []}
axis_x_F = {'line_1': [0], 'line_2': [0], 'line_3': [0], 'line_4': [0], 'line_5': [0]}
axis_y_F = {'line_1': [0], 'line_2': [0], 'line_3': [0], 'line_4': [0], 'line_5': [0]}
for line in acc:
    for n in p_win_dict_new_keys_and_values[line]:
        axis_x[line].append(n)
        axis_y[line].append(p_win_dict_new_keys_and_values[line][n] / acc[line])
        axis_x_F[line].append(n)
        axis_y_F[line].append(axis_y_F[line][len(axis_y_F[line]) - 1] + p_win_dict_new_keys_and_values[line][n] / acc[line])

figure = go.Figure()
for line in acc:
    figure.add_trace(go.Scatter(x=axis_x[line], y=axis_y[line]))
figure.show()
figure = go.Figure()
for line in acc:
    figure.add_trace(go.Scatter(x=axis_x_F[line], y=axis_y_F[line]))
figure.show()

EV_N_ACTUAL = [sum(EV_list[0]) / len(EV_list[0]),
               sum(EV_list[1]) / len(EV_list[1]),
               sum(EV_list[2]) / len(EV_list[2]),
               sum(EV_list[3]) / len(EV_list[3]),
               sum(EV_list[4]) / len(EV_list[4]),]

debug = 0