import alignments
from random_sequences import generate_dna_sequences
from time import time
import json

# Globals
delta = alignments.delta_edit_distance()


def time_nw(s1, s2):
    t1 = time()
    out = alignments.align_needleman_wunsch(s1, s2, delta)
    t2 = time()
    return t2 - t1


def time_banded(s1, s2, k):
    t1 = time()
    out = alignments.align_banded_global(s1, s2, k, delta)
    t2 = time()
    return t2 - t1


lengths = [25, 50, 100, 250, 500, 750, 1000, 2000, 3000, 4000, 5000]
bandwidths = [1, 3, 5, 10, 20]

s = 0.75  # Similarity score for random strings

D = {}  # length -> ("NW"/"BW" -> time)
for length in lengths:
    D[length] = {}
    s1, s2 = generate_dna_sequences(length, s)
    D[length]["NW"] = 0
    for i in range(10):
        D[length]["NW"] += time_nw(s1, s2) / 10
    for k in bandwidths:
        D[length][str(k)] = 0
        D[length][str(k)] = time_banded(s1, s2, k)
        for i in range(10):
            D[length][str(k)] += time_banded(s1, s2, k) / 10


with open("times.json", "w") as outfile:
    json.dump(D, outfile)
