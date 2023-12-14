import pytest
import alignments


# All needleman wunsch examples generated and validated at https://valiec.github.io/AlignmentVisualizer/index.html
# All banded examples generated and validated by hand according to banded sequence recurrence


# Globals
delta = alignments.delta_edit_distance()


def test_nw_identical():
    assert alignments.align_needleman_wunsch("ACGT", "ACGT", delta) == (4, "ACGT\nACGT")


def test_nw_basic_mismatch():
    assert alignments.align_needleman_wunsch("ACGT", "ACCT", delta) == (2, "ACGT\nACCT")


def test_nw_mismatch1():
    assert alignments.align_needleman_wunsch("ACGTTCGA", "ACCTAGGG", delta) == (
        0,
        "ACGTTCGA\nACCTAGGG",
    )


def test_nw_mismatch2():
    assert alignments.align_needleman_wunsch("TTTACGTTCGA", "CAGACCTAGGG", delta) == (
        -3,
        "TTTACGTTCGA\nCAGACCTAGGG",
    )


def test_nw_mismatch3():
    assert alignments.align_needleman_wunsch("AAAAAA", "CGAGAA", delta) == (
        0,
        "AAAAAA\nCGAGAA",
    )


def test_nw_gap1():
    assert alignments.align_needleman_wunsch("GAAAA", "AAAAT", delta) == (
        2,
        "GAAAA-\n-AAAAT",
    )


def test_nw_gap2():
    assert alignments.align_needleman_wunsch("GAAAAACGTTC", "AAAATATGCAT", delta) == (
        1,
        "GAAAA-ACGT-TC\n-AAAATATGCAT-",
    )


def test_nw_gap3():
    assert alignments.align_needleman_wunsch("ATCGA", "TTGAC", delta) == (
        0,
        "ATCGA-\nTT-GAC",
    )


def test_nw_score1():
    assert (
        alignments.align_needleman_wunsch(
            "GGAACGGCGCGTCCTGCGCA", "GGAAAGTTTTGCTCTAGGCA", delta
        )[0]
        == 5
    )


def test_nw_score2():
    assert (
        alignments.align_needleman_wunsch(
            "CCTTCAGCCACCCCGTCTCGATACT", "GCTTCATCCACCCATATCGGGAAAC", delta
        )[0]
        == 9
    )


def test_nw_score3():
    assert (
        alignments.align_needleman_wunsch(
            "GTCCATAATTGACAAACGCGACACAGATCCAGTGTCGAGATAGGCGGCTG",
            "GCCTACAATTTACAAACGCGACACAGATCCAGTGTTATGATAGGCGGCTG",
            delta,
        )[0]
        == 38
    )


def test_banded_match():
    s1 = "ACTGTGT"
    s2 = "ACTGTGT"
    for k in range(5):
        assert alignments.align_banded_global(s1, s2, k, delta) == (
            7,
            "ACTGTGT\nACTGTGT",
        )


def test_banded_k0():
    s1 = "ACTGTGT"
    s2 = "TGAAAAA"
    assert alignments.align_banded_global(s1, s2, 0, delta) == (
        -7,
        "ACTGTGT\nTGAAAAA",
    )


def test_banded_k1():
    s1 = "ACTGTA"
    s2 = "TGATGT"
    assert alignments.align_banded_global(s1, s2, 1, delta) == (-1, "AC-TGTA\nTGATGT-")


def test_banded_k2():
    s1 = "ACTGTA"
    s2 = "TGATGT"
    assert alignments.align_banded_global(s1, s2, 2, delta) == (0, "--ACTGTA\nTGA-TGT-")


def test_banded_k3():
    s1 = "ACTGTAGTTGTTG"
    s2 = "TGATGTACAAACT"
    assert alignments.align_banded_global(s1, s2, 3, delta) == (
        -3,
        "--ACTGTAGTTGTTG\nTGA-TGTACAAACT-",
    )
