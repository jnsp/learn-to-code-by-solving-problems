# https://usaco.org/index.php?page=viewproblem2&cpid=987


def edit(words: str, width: int) -> list[str]:
    list_words = words.split()
    result = list()
    line = ""

    for word in list_words:
        if len(line.replace(" ", "")) + len(word) > width:
            result.append(line[:-1])
            line = ""
        line += word + " "

    # flush rest of words
    result.append(line[:-1])

    return result
