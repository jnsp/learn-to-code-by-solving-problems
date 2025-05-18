# USACO 2017 US Open Contest, Bronze
# Problem 2. Bovine Genomics
# https://usaco.org/index.php?page=viewproblem2&cpid=736


def count_positions(spotty_genes: tuple[str, ...], plain_genes: tuple[str, ...]) -> int:
    result = 0
    n_positions = len(spotty_genes[0])

    for i in range(n_positions):
        spotty_position = set()
        for spotty_gene in spotty_genes:
            spotty_position.add(spotty_gene[i])

        plain_position = set()
        for plain_gene in plain_genes:
            plain_position.add(plain_gene[i])

        if spotty_position.isdisjoint(plain_position):
            result += 1

    return result
