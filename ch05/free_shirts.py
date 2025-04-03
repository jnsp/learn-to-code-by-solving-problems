# https://dmoj.ca/problem/ecoo19r1p1


def laundry(n_shirts: int, days: int, event_days: list[int]) -> int:
    clean_shirts = n_shirts
    n_laundry = 0

    for day in range(1, days + 1):
        # do laundry
        if clean_shirts == 0:
            n_laundry += 1
            clean_shirts = n_shirts

        # wear a shirt
        clean_shirts -= 1

        # get free shirts
        if day in event_days:
            free_shirts = event_days.count(day)
            n_shirts += free_shirts
            clean_shirts += free_shirts

    return n_laundry


if __name__ == "__main__":
    for _ in range(10):
        n_shirts, n_events, days = [int(i) for i in input().split()]
        event_days = [int(i) for i in input().split()]
        assert len(event_days) == n_events
        print(laundry(n_shirts, days, event_days))
