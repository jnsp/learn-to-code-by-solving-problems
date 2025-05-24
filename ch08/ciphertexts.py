# https://dmoj.ca/problem/ccc06s2

from string import ascii_uppercase


def infer_last_one(mapping_table: dict[str, str]) -> dict[str, str]:
    all_letters = ascii_uppercase + " "

    if len(mapping_table) == (len(all_letters) - 1):
        last_one_cipher = set(all_letters) - set(mapping_table.keys())
        last_one_plain = set(all_letters) - set(mapping_table.values())
        mapping_table[last_one_cipher.pop()] = last_one_plain.pop()

    return mapping_table


def decrypt(plain_text: str, cipher_text: str, to_decrypt: str) -> str:
    mapping_table = {c: p for c, p in zip(cipher_text, plain_text)}
    mapping_table = infer_last_one(mapping_table)
    return "".join(mapping_table.get(d, ".") for d in to_decrypt)


if __name__ == "__main__":
    plain_text = input()
    cipher_text = input()
    to_decrypt = input()

    print(decrypt(plain_text, cipher_text, to_decrypt))
