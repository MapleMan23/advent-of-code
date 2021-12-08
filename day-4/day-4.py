import numpy as np

with open("day-4/day-4-input.txt") as f:
    draws = f.readline()
    boards = [line.strip().split() for line in f.readlines() if len(line) > 1]

draws = [int(x) for x in draws.split(",")]

boards = np.array(boards, dtype=int)
boards = boards.reshape(-1, 5, 5)


def row_winner(boards):
    wins = (boards == -1).all(2).any(1)
    if wins.any():
        return wins.argmax()
    else:
        return -1


def col_winner(boards):
    wins = (boards == -1).all(1).any(1)
    if wins.any():
        return wins.argmax()
    else:
        return -1


rows, cols = -1, -1
winning_board = -1
last_draw = 0
for d in draws:
    boards[boards == d] = -1
    rows = row_winner(boards)
    cols = col_winner(boards)

    if rows > 0:
        winning_board = rows
        break
    elif cols > 0:
        winning_board = cols
        break

    last_draw = d

winner = boards[winning_board]

s = winner[winner != -1].sum()
print(s * last_draw, winning_board)