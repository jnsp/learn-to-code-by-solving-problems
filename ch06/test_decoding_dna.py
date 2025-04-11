from decoding_dna import find_rna, find_terminator, find_to_transcribe, flip, rna


def test_flip():
    sequence = "ATCAAGGCCTATTCCGGGAAAGG"
    assert flip(sequence) == "TAGTTCCGGATAAGGCCCTTTCC"


def test_find_to_transcribe():
    sequence = "AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC"
    assert find_to_transcribe(sequence) == "GGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC"


def test_find_terminator():
    sequence = "GGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC"
    assert find_terminator(sequence) == "GTCATG"


def test_find_rna():
    candidate = "GGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC"
    terminator = "GTCATG"
    assert find_rna(candidate, terminator) == "CCUAAAUCUAACUGGG"


def test_rna():
    sequence = "AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC"
    assert rna(sequence) == "CCUAAAUCUAACUGGG"

    sequence = "AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA"
    assert rna(sequence) == "UAGCGCUGCUUUAU"

    sequence = "TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT"
    assert rna(sequence) == "CUCUCUGGCUCACAAAUUC"
