# https://dmoj.ca/problem/ccc06j1


def calorie(burger: int, side: int, drink: int, dessert: int) -> int:
    burger_calories = {1: 461, 2: 431, 3: 420, 4: 0}
    side_calories = {1: 100, 2: 57, 3: 70, 4: 0}
    drink_calories = {1: 130, 2: 160, 3: 118, 4: 0}
    dessert_calories = {1: 167, 2: 266, 3: 75, 4: 0}

    return burger_calories[burger] + side_calories[side] + drink_calories[drink] + dessert_calories[dessert]


if __name__ == "__main__":
    burger = int(input())
    side = int(input())
    drink = int(input())
    dessert = int(input())

    calorie_sum = calorie(burger, side, drink, dessert)
    print(f"Your total Calorie count is {calorie_sum}.")
