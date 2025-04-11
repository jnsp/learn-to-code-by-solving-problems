# https://dmoj.ca/problem/ccc18j3


def read_distances() -> list[int]:
    distances = [int(value) for value in input().split()]
    return distances


def distances_from_origin(distances: list[int]) -> list[int]:
    distances_from_origin = [0]

    for distance in distances:
        distances_from_origin.append(distances_from_origin[-1] + distance)

    return distances_from_origin


def distances_between_cities(distances_from_origin: list[int]) -> list[list[int]]:
    distances = [distances_from_origin[:]]

    for city_position in distances_from_origin[1:]:
        distances_from_city = [abs(city_position - distance) for distance in distances_from_origin]
        distances.append(distances_from_city)

    return distances


def main():
    distances = read_distances()
    positions_cities = distances_from_origin(distances)
    result = distances_between_cities(positions_cities)

    for distances_from_each_city in result:
        print(*distances_from_each_city)


if __name__ == "__main__":
    main()
