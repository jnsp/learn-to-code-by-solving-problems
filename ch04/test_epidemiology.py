from epidemiology import days_infected_all


def test_infected_4days():
    population = 750
    infected = 1
    daily_infections = 5
    assert days_infected_all(population, infected, daily_infections) == 4


def test_infected_5days():
    population = 10
    infected = 2
    daily_infections = 1
    assert days_infected_all(population, infected, daily_infections) == 5
