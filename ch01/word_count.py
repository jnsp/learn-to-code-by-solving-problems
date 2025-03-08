# https://dmoj.ca/problem/dmopc15c7p2


def word_count(input_string):
    total_words = input_string.count(" ")
    if input_string:
        total_words += 1

    return total_words


if __name__ == "__main__":
    input_string = input("")
    print(word_count(input_string))
