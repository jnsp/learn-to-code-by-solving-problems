# https://dmoj.ca/problem/ccc13s1


def is_distinct(year: int) -> bool:
    year_str = list(str(year))
    return len(year_str) == len(set(year_str))


def next_distinct_year(year: int) -> int:
    while True:
        year += 1
        if is_distinct(year):
            return year


def read_year():
    year = int(input())
    return year


def main():
    year = read_year()
    result = next_distinct_year(year)
    print(result)


if __name__ == "__main__":
    main()
