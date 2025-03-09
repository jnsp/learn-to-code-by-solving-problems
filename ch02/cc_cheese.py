# https://dmoj.ca/problem/dmopc16c1p0


def cc_cheese(width_pizza: int, pct_cheese: int) -> str:
    if width_pizza == 3 and pct_cheese >= 95:
        return "absolutely"
    elif width_pizza == 1 and pct_cheese <= 50:
        return "fairly"
    else:
        return "very"


if __name__ == "__main__":
    width_pizza = int(input())
    pct_cheese = int(input())
    satisfaction = cc_cheese(width_pizza, pct_cheese)
    print(f"C.C. is {satisfaction} satisfied with her pizza.")
