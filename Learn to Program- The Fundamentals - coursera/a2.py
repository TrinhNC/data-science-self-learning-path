def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count_ = 0
    for nuc in dna:
        if nuc == nucleotide:
            count_ = count_ + 1
    return count_


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (i.e. ontains no characters other than ’A’, ’T’, ’C’ and ’G’)

    >>> is_valid_sequence('TTT')
    True

    >>> is_valid_sequence('TGCAGDA')
    False
    """
    is_correct = True
    for nuc in dna:
        if nuc != 'A' and nuc != 'T' and nuc != 'C' and nuc != 'G':
            is_correct = False
            break
    return is_correct

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence
    at the given index.

    >>> insert_sequence('CCGG','AT', 2)
    'CCATGG'

    """
    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nuc):
    """ (str) -> str

    Return the nucleotide's complement

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    """
    if nuc == 'A':
        return 'T'
    elif nuc == 'T':
        return 'A'
    elif nuc == 'C':
        return 'G'
    elif nuc == 'G':
        return 'C'
    else:
        print("nucleotite should be 1 letter among 'A','T','C','G'")


def get_complementary_sequence(dna1):
    """(str)->str

    Return a DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('TACG')
    'ATGC'

    """
    dna2 = ''
    for nuc in dna1:
        dna2 = dna2 + get_complement(nuc)
    return dna2