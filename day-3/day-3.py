import numpy as np
import pandas as pd

with open("day-3/day-3-input.txt") as f:
    bits = [list(line.strip()) for line in f.readlines()]
bits = pd.DataFrame(bits).astype(int)

gamma = bits.mode().astype(bool).values.squeeze()
eps = ~gamma

gamma = int("".join([str(x) for x in gamma.astype(int)]), 2)
eps = int("".join([str(x) for x in eps.astype(int)]), 2)

print(gamma * eps)


# Part 2
oxygen = bits.copy()
ind = 0
while len(oxygen) > 1:
    m = oxygen.iloc[:, ind].mode()
    if len(m) > 1:
        m = 1
    else:
        m = m.item()
    mask = oxygen.iloc[:, ind] == m
    oxygen = oxygen.loc[mask]
    ind += 1

oxygen = oxygen.values.squeeze()
oxygen = int("".join([str(x) for x in oxygen.astype(int)]), 2)

co2 = bits.copy()
ind = 0
while len(co2) > 1:
    m = co2.iloc[:, ind].mode()
    if len(m) > 1:
        m = 0
    else:
        m = int(not bool(m.item()))
    mask = co2.iloc[:, ind] == m
    co2 = co2.loc[mask]
    ind += 1

co2 = co2.values.squeeze()
co2 = int("".join([str(x) for x in co2.astype(int)]), 2)

print(oxygen * co2)