# https://dmoj.ca/problem/ccc20j2


def days_infected_all(population: int, infected: int, daily_infections: int) -> int:
    days = 0
    new_infected = infected
    while infected <= population:
        new_infected *= daily_infections
        infected += new_infected
        days += 1

    return days


if __name__ == "__main__":
    population = int(input())
    infected = int(input())
    daily_infections = int(input())
    print(days_infected_all(population, infected, daily_infections))
