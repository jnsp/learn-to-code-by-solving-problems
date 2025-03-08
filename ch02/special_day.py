# https://dmoj.ca/problem/ccc15j1
from datetime import date


def special_day(month: int, day: int) -> str:
    if month == 2 and day == 18:
        return "Special"
    elif month < 2 or (month == 2 and day < 18):
        return "Before"
    else:
        return "After"


def special_day2(month: int, day: int) -> str:
    special = date(2015, 2, 18)
    current = date(2015, month, day)

    if current == special:
        return "Special"
    elif current < special:
        return "Before"
    else:
        return "After"


if __name__ == "__main__":
    month = int(input())
    day = int(input())
    print(special_day2(month, day))
