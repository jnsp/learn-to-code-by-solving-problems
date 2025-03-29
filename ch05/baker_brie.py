# https://dmoj.ca/problem/ecoo17r3p1


class Bakery:
    def __init__(self):
        self.sales: list[list[int]] = []
        self.bonus = 0

    def insert_sales(self, sales: list[int]):
        self.sales.append(sales)

    def _add_bonus(self, sales: list[list[int]]):
        for sale in sales:
            if (total_sale := sum(sale)) % 13 == 0:
                self.bonus += total_sale // 13

    def get_bonus(self) -> int:
        self._add_bonus(self.sales)
        transoposed_sales = [list(i) for i in zip(*self.sales)]
        self._add_bonus(transoposed_sales)

        return self.bonus


if __name__ == "__main__":
    for _ in range(10):
        lst = input().split()
        n_franchisees = int(lst[0])
        days = int(lst[1])

        bakery = Bakery()

        for _ in range(days):
            sale = input().split()
            sale = [int(s) for s in sale]
            bakery.insert_sales(sale)

        print(bakery.get_bonus())
