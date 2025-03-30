# https://dmoj.ca/problem/ecoo18r1p1


def waiting_days(play_days: int, shoppings: list[str]) -> int:
    boxes: list[str] = []

    for item in shoppings:
        if item == "B":
            boxes += ["B"] * play_days
        if boxes:
            boxes.pop()

    return len(boxes)


if __name__ == "__main__":
    for _ in range(10):
        play_days, shopping_days = [int(v) for v in input().split()]
        shoppings = [input() for _ in range(shopping_days)]
        print(waiting_days(play_days, shoppings))
