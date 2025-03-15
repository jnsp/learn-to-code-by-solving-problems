# https://dmoj.ca/problem/wc17c3j3
from string import ascii_lowercase, ascii_uppercase, digits


def valid_password(password):
    if not (8 <= len(password) <= 12):
        return "Invalid"

    n_lowercases = 0
    n_uppercases = 0
    n_digits = 0

    for char in password:
        if char in ascii_lowercase:
            n_lowercases += 1
        elif char in ascii_uppercase:
            n_uppercases += 1
        elif char in digits:
            n_digits += 1

    if n_lowercases >= 3 and n_uppercases >= 2 and n_digits >= 1:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    password = input()
    print(valid_password(password))
