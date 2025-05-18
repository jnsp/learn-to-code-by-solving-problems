# USACO 2018 US Open Contest, Bronze
# Problem 1. Team Tic Tac Toe
# https://usaco.org/index.php?page=viewproblem2&cpid=831


def count_winners(board: tuple[str, ...]) -> tuple[int, int]:
    h1 = frozenset(board[0])
    h2 = frozenset(board[1])
    h3 = frozenset(board[2])
    v1 = frozenset(board[0][0] + board[1][0] + board[2][0])
    v2 = frozenset(board[0][1] + board[1][1] + board[2][1])
    v3 = frozenset(board[0][2] + board[1][2] + board[2][2])
    d1 = frozenset(board[0][0] + board[1][1] + board[2][2])
    d2 = frozenset(board[0][2] + board[1][1] + board[2][0])

    comb = {h1, h2, h3, v1, v2, v3, d1, d2}

    solo_winners = 0
    team_winners = 0

    for c in comb:
        if len(c) == 1:
            solo_winners += 1
        if len(c) == 2:
            team_winners += 1

    return solo_winners, team_winners
