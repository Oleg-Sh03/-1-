# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

print("Введите число журавликов, сделанных детьми (число кратное трём):")
s = int(input())
if s % 3 == 0:
    print(s, "->", s / 3, (s / 3) * 2, s / 3)
else:
    print("Задача не имеет решения")