# https://dmoj.ca/problem/coci13c2p2

from itertools import product


class Church:
    def __init__(self, n_rows: int | None = None, n_columns: int | None = None, benches: list[str] | None = None):
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.benches = benches

    def read_benches(self):
        self.benches = list()
        self.n_rows, self.n_columns = [int(value) for value in input().split()]

        for _ in range(self.n_rows):
            row = input()
            assert len(row) == self.n_columns
            self.benches.append(row)

    def get_neighbors_positions(self, location: tuple[int, int]) -> set[tuple[int, int]]:
        assert self.n_rows is not None
        assert self.n_columns is not None

        neighbors_positions = set()

        for row, col in product([-1, 0, 1], repeat=2):
            if row == col == 0:
                continue

            neighbor_row = location[0] + row
            neighbor_col = location[1] + col

            if (0 <= neighbor_row < self.n_rows) and (0 <= neighbor_col < self.n_columns):
                neighbors_positions.add((neighbor_row, neighbor_col))

        return neighbors_positions

    def is_occupied(self, location: tuple[int, int]) -> bool:
        assert self.benches is not None

        row, col = location
        mark = self.benches[row][col]
        return mark == "o"

    def get_handshakes_with_neighbors(self, row: int, col: int) -> set[tuple[int, int]]:
        handshakes = set()
        neighbors_positions = self.get_neighbors_positions((row, col))

        for neighbor_row, neighbor_col in neighbors_positions:
            if self.is_occupied((neighbor_row, neighbor_col)):
                new_handshake = frozenset(((row, col), (neighbor_row, neighbor_col)))
                handshakes.add(new_handshake)

        return handshakes

    def handshakes(self) -> int:
        assert self.n_rows is not None
        assert self.n_columns is not None

        all_handshakes = set()
        max_extra_handshakes = 0

        for row in range(self.n_rows):
            for col in range(self.n_columns):
                handshakes = self.get_handshakes_with_neighbors(row, col)

                if self.is_occupied((row, col)):
                    all_handshakes.update(handshakes)
                else:
                    max_extra_handshakes = max(max_extra_handshakes, len(handshakes))

        return len(all_handshakes) + max_extra_handshakes


if __name__ == "__main__":
    church = Church()
    church.read_benches()
    print(church.handshakes())
