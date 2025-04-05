# https://dmoj.ca/problem/ecoo18r1p2


def minimum_roundabout(routes: dict[int, list[int]]) -> tuple[int, list[int]]:
    mins_routes = {route: min(diameters) for route, diameters in routes.items()}
    min_roundabout = min(mins_routes.values())
    routes_with_min = sorted(route for route, min_diameter in mins_routes.items() if min_diameter == min_roundabout)
    return min_roundabout, routes_with_min


if __name__ == "__main__":
    for _ in range(10):
        n_routes = int(input())
        routes = dict()
        for _ in range(n_routes):
            route, _, *diameters = input().split()
            routes[int(route)] = [int(d) for d in diameters]

        min_roundabout, routes_with_min = minimum_roundabout(routes)
        routes_with_min = [str(i) for i in routes_with_min]
        print(min_roundabout, f"{{{','.join(routes_with_min)}}}")
