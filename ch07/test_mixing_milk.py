from mixing_milk import Bucket, pour_bucket, pour_ntimes


def test_bucket():
    bucket = Bucket(10, 3)
    assert bucket.capacity == 10
    assert bucket.milk == 3
    assert bucket.available == 7


def test_pour_with_enough_capacity():
    bucket1 = Bucket(10, 3)
    bucket2 = Bucket(11, 4)

    pour_bucket(bucket1, bucket2)

    assert bucket1.milk == 0
    assert bucket2.milk == 7


def test_pour_with_lack_capacity():
    bucket1 = Bucket(10, 8)
    bucket2 = Bucket(11, 4)

    pour_bucket(bucket1, bucket2)

    assert bucket1.milk == 1
    assert bucket2.milk == 11


def test_pour_ntimes():
    bucket1 = Bucket(10, 3)
    bucket2 = Bucket(11, 4)
    bucket3 = Bucket(12, 5)

    assert pour_ntimes((bucket1, bucket2, bucket3)) == (0, 10, 2)


def test_pour_ntimes_large():
    bucket1 = Bucket(855636227, 749698587)
    bucket2 = Bucket(687926653, 660260757)
    bucket3 = Bucket(959997302, 485560281)

    assert pour_ntimes((bucket1, bucket2, bucket3)) == (381199206, 687926653, 826393766)
