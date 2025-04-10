# https://acm.timus.ru/problem.aspx?space=1&num=2144


def read_box():
    n_boxes = int(input())
    boxes = []
    for _ in range(n_boxes):
        box = [int(value) for value in input().split()]
        boxes.append(box[1:])
    return boxes


def box_ok(box: list[int]) -> bool:
    for i in range(len(box) - 1):
        if box[i] > box[i + 1]:
            return False

    return True


def endpoints(boxes: list[list[int]]) -> list[list[int]]:
    return [[box[0], box[-1]] for box in boxes]


def check_endpoints(sorted_endpoints: list[list[int]]) -> bool:
    maximum = sorted_endpoints[0][1]
    for box in sorted_endpoints[1:]:
        if box[0] < maximum:
            return False
        maximum = box[1]
    return True


def main():
    boxes = read_box()

    for box in boxes:
        if not box_ok(box):
            print("NO")
            return

    endpoints_list = endpoints(boxes)
    endpoints_list.sort()

    if check_endpoints(endpoints_list):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
