import pytest
from bovine_genomics import count_positions


@pytest.mark.parametrize(
    "spotty_genes, plain_genes, expected",
    [
        (
            ("AATCCCAT", "GATTGCAA", "GGTCGCAA"),
            ("ACTCCCAG", "ACTCGCAT", "ACTTCCAT"),
            1,
        ),
        (
            ("TTTGA", "TATCT", "TTCGC"),
            ("AGGAG", "GCGGG", "AGGTG"),
            4,
        ),
        (
            ("GGTTGGCCGC", "AAACAGCCCA", "TACTCCCTCT", "TACCGCCTTG", "AATACGCGTC"),
            ("TTAAAAGAAG", "TATTTTAATC", "ATTGCTTCGA", "TTACAATTCG", "GAAGAAAATG"),
            2,
        ),
    ],
)
def test_count_positions(spotty_genes, plain_genes, expected):
    assert count_positions(spotty_genes, plain_genes) == expected
