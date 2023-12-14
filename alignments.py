import pprint

# Traceback and Global Alignment code based on CS466 HW 1 (Fall 2023 - Prof. Mohammed El-Kebir)


# Global coordinate variables for traceback
UP = (-1, 0)
LEFT = (0, -1)
TOPLEFT = (-1, -1)
ORIGIN = (0, 0)
N_INF = (float("-inf"), float("-inf"))


def traceback_global(v, w, pointers):
    i, j = len(v), len(w)
    new_v = []
    new_w = []
    while True:
        di, dj = pointers[i][j]
        if (di, dj) == LEFT:
            new_v.append("-")
            new_w.append(w[j - 1])
        elif (di, dj) == UP:
            new_v.append(v[i - 1])
            new_w.append("-")
        elif (di, dj) == TOPLEFT:
            new_v.append(v[i - 1])
            new_w.append(w[j - 1])
        i, j = i + di, j + dj
        if i <= 0 and j <= 0:
            break
    return "".join(new_v[::-1]) + "\n" + "".join(new_w[::-1])


def align_needleman_wunsch(v, w, delta):
    """
    Returns the score of the maximum scoring alignment of the strings v and w, as well as the actual alignment as
    computed by traceback_global.

    :param: v
    :param: w
    :param: delta
    """
    M = [[0 for j in range(len(w) + 1)] for i in range(len(v) + 1)]
    pointers = [[N_INF for j in range(len(w) + 1)] for i in range(len(v) + 1)]
    score, alignment = None, None

    for i in range(len(v) + 1):
        for j in range(len(w) + 1):
            if i == 0 and j == 0:
                M[i][j] = 0
                pointers[i][j] = ORIGIN

            elif j == 0:
                M[i][j] = M[i - 1][j] + delta[v[i - 1]]["-"]
                pointers[i][j] = UP

            elif i == 0:
                M[i][j] = M[i][j - 1] + delta["-"][w[j - 1]]
                pointers[i][j] = LEFT

            else:
                l = M[i][j - 1] + delta["-"][w[j - 1]]
                u = M[i - 1][j] + delta[v[i - 1]]["-"]
                tl = M[i - 1][j - 1] + delta[v[i - 1]][w[j - 1]]

                if l == max(l, u, tl):
                    M[i][j] = l
                    pointers[i][j] = LEFT
                elif u == max(l, u, tl):
                    M[i][j] = u
                    pointers[i][j] = UP
                else:
                    M[i][j] = tl
                    pointers[i][j] = TOPLEFT

    score = M[len(v)][len(w)]
    alignment = traceback_global(v, w, pointers)
    return score, alignment


def align_banded_global(v, w, k, delta):
    """
    Returns the score of the maximum scoring alignment of the strings v and w, as well as the actual alignment as
    computed by traceback_global.

    :param: v
    :param: w
    :param: delta
    """

    if len(v) != len(w):
        raise Exception("Strings v and w must be same length.")

    v_len = len(v) + 1
    w_len = len(w) + 1
    M = [[0 for j in range(w_len)] for i in range(v_len)]
    pointers = [[N_INF for j in range(w_len)] for i in range(v_len)]
    score, alignment = None, None

    for i in range(v_len):
        for j in range(max(0, i - k), min(w_len, i + k + 1)):
            if i == 0 and j == 0:
                M[i][j] = 0
                pointers[i][j] = ORIGIN

            elif j == 0:
                M[i][j] = M[i - 1][j] + delta[v[i - 1]]["-"]
                pointers[i][j] = UP

            elif i == 0:
                M[i][j] = M[i][j - 1] + delta["-"][w[j - 1]]
                pointers[i][j] = LEFT

            else:
                valid_neighbors = []
                # Left
                if in_band(i, j - 1, k):
                    l = M[i][j - 1] + delta["-"][w[j - 1]]
                    valid_neighbors.append((l, LEFT))
                # Up
                if in_band(i - 1, j, k):
                    u = M[i - 1][j] + delta[v[i - 1]]["-"]
                    valid_neighbors.append((u, UP))
                # Top left
                if in_band(i - 1, j - 1, k):
                    tl = M[i - 1][j - 1] + delta[v[i - 1]][w[j - 1]]
                    valid_neighbors.append((tl, TOPLEFT))

                m, p = max(valid_neighbors)
                M[i][j] = m
                pointers[i][j] = p

    score = M[len(v)][len(w)]
    alignment = traceback_global(v, w, pointers)
    return score, alignment


def in_band(i, j, k):
    return abs(i - j) <= k


def delta_edit_distance():
    keys = ["A", "C", "T", "G", "-"]
    delta = {}
    for i in range(len(keys)):
        delta[keys[i]] = {
            k: v
            for (k, v) in zip(
                keys, [1 if keys[i] == keys[j] else -1 for j in range(len(keys))]
            )
        }
    return delta


def print_dp_table(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:4d}", end=" ")
        print()
