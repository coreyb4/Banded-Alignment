import random


def generate_dna_sequences(length, similarity_score):
    alphabet = ["A", "C", "G", "T"]

    # Generate the initial identical sequence
    sequence1 = "".join(random.choice(alphabet) for _ in range(length))
    sequence2 = sequence1[:]

    # Calculate the number of edits needed
    num_edits = int((1 - similarity_score) * length)
    random_ints = random.sample(range(length), num_edits)
    # Perform edits
    for idx in random_ints:
        new_base = random.choice([base for base in alphabet if base != sequence1[idx]])
        sequence2 = sequence2[:idx] + new_base + sequence2[idx + 1 :]

    return sequence1, sequence2
