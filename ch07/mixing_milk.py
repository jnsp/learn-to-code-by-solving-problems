# USACO 2018 December Contest, Bronze
# Problem 1. Mixing Milk
# https://usaco.org/index.php?page=viewproblem2&cpid=855

from dataclasses import dataclass
from itertools import cycle, pairwise


@dataclass
class Bucket:
    capacity: int
    milk: int

    @property
    def available(self):
        return self.capacity - self.milk


def pour_bucket(source: Bucket, target: Bucket) -> None:
    milk_to_pour = min(source.milk, target.available)
    source.milk -= milk_to_pour
    target.milk += milk_to_pour


def pour_ntimes(buckets: tuple[Bucket, ...], n: int = 100) -> tuple[int, ...]:
    bucket_cycle = cycle(buckets)
    bucket_pairs = pairwise(bucket_cycle)

    for _ in range(n):
        source, target = next(bucket_pairs)
        pour_bucket(source, target)

    return tuple(bucket.milk for bucket in buckets)
