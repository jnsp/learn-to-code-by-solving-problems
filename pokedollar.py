# https://dmoj.ca/problem/wc18c3j1


def pokedollar(total_paint, paint_for_badge, badge_price):
    badges, remaining_paint = divmod(total_paint, paint_for_badge)
    return badges * badge_price + remaining_paint


if __name__ == "__main__":
    p = int(input())
    b = int(input())
    d = int(input())
    print(pokedollar(p, b, d))
