# https://dmoj.ca/problem/crci07p1

from dataclasses import dataclass


@dataclass(order=True)
class Platform:
    altitude: int
    left_pos: int
    right_pos: int

    @property
    def left_pillar(self):
        return self.left_pos + 0.5

    @property
    def right_pillar(self):
        return self.right_pos - 0.5

    def __sub__(self, other):
        if isinstance(other, Platform):
            return self.altitude - other.altitude

        return NotImplemented


def length_of_pillars(target_platform: Platform, platforms: list[Platform]) -> int:
    ground = Platform(0, 0, 10_000)
    max_left_platform = ground
    max_right_platform = ground

    for platform in platforms + [ground]:
        if not target_platform > platform:
            continue

        if platform.left_pos < target_platform.left_pillar < platform.right_pos:
            max_left_platform = platform if platform > max_left_platform else max_left_platform

        if platform.left_pos < target_platform.right_pillar < platform.right_pos:
            max_right_platform = platform if platform > max_right_platform else max_right_platform

    left_pillar = target_platform - max_left_platform
    right_pillar = target_platform - max_right_platform

    return left_pillar + right_pillar


def total_length(platforms: list[Platform]) -> int:
    length = 0
    for platform in platforms:
        length += length_of_pillars(platform, platforms)
    return length


def main():
    platforms = list()
    n_platforms = int(input())
    for _ in range(n_platforms):
        platform = Platform(*(int(value) for value in input().split()))
        platforms.append(platform)

    length = total_length(platforms)
    print(length)


if __name__ == "__main__":
    main()
