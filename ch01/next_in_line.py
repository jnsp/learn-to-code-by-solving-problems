# https://dmoj.ca/problem/ccc13j1


def next_in_line(youngest_age, middle_age):
    return middle_age + (middle_age - youngest_age)


if __name__ == "__main__":
    y = int(input())
    m = int(input())
    print(next_in_line(y, m))
