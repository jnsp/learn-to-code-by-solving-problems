# https://dmoj.ca/problem/ecoo12r1p2


def flip(sequence: str) -> str:
    complementary = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complementary[base] for base in sequence])


def find_to_transcribe(sequence: str) -> str:
    promoter = "TATAAT"
    index = sequence.find(promoter)
    return sequence[index + 10 :]


def find_terminator(sequence: str) -> str:
    for start_index in range(len(sequence) - 5):
        length = 6
        end_index = start_index + length

        search_sequence = sequence[start_index:end_index]
        reversed_complementary = flip(search_sequence)[::-1]

        if reversed_complementary in sequence[end_index:]:
            return search_sequence

    raise ValueError("There is no terminator!")


def find_rna(candidate: str, terminator: str) -> str:
    complementary = {"A": "U", "T": "A", "C": "G", "G": "C"}
    index = candidate.find(terminator)
    to_transcribe = candidate[:index]
    return "".join(complementary[base] for base in to_transcribe)


def rna(sequnce: str) -> str:
    candidate = find_to_transcribe(sequnce)
    terminator = find_terminator(candidate)
    rna = find_rna(candidate, terminator)
    return rna


if __name__ == "__main__":
    for i in range(1, 6):
        sequence = input()
        result = rna(sequence)
        print(f"{i}: {result}")
