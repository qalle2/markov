# generate random strings based on source data using a character-level Markov
# chain;
# "order" = how many previous characters affect each new character

import os, random, re, sys

# if 0, print random strings; if 1, print stats on source data
DEBUG_MODE = 0

# minimum length of random strings to print (if DEBUG=0)
MIN_RANDOM_LENGTH = 4

# ignore random strings that occur in original strings (0=no, 1=yes)
IGNORE_ORIG = 1

# how many random strings to print (if DEBUG=0)
RANDOM_COUNT = 50

def get_orig_strings(filename, order):
    # generate original strings from file;
    # order: order of Markov chain

    with open(filename, "rt") as handle:
        handle.seek(0)
        for line in handle:
            stri = line.rstrip("\n")
            if len(stri) < order - 1:
                print(
                    "Warning: skipping original string (too short): " + stri,
                    file=sys.stderr
                )
            if re.search(r"^[A-ZÅÄÖÜa-zåäößü &'.-]+$", stri) is None:
                sys.exit("Invalid characters in original string: " + stri)
            yield stri

def get_probs(origStrs, order):
    # origStrs: original strings (iterable)
    # order: order of Markov chain
    # return: probabilities (dict, see below)

    probs = {}  # {previous_character(s): {character: count, ...}, ...}

    for stri in origStrs:
        stri = "_" + stri + "_"  # "_" = start/end
        for i in range(order, len(stri)):
            char = stri[i]
            prev = stri[i-order:i]
            if prev not in probs:
                probs[prev] = {}
            if char not in probs[prev]:
                probs[prev][char] = 0
            probs[prev][char] += 1

    return probs

def get_random_string(probs):
    # get a random string based on probabilities

    # first characters to output; also the initial previous substring for the
    # following loop
    prevSubstrs = sorted(c for c in probs if c.startswith("_"))
    prevSubstrWeights = tuple(sum(probs[c].values()) for c in prevSubstrs)
    prevSubstr = random.choices(prevSubstrs, weights=prevSubstrWeights)[0]
    yield prevSubstr[1:]

    # the rest of the characters, one by one
    while True:
        chars = sorted(probs[prevSubstr])
        charWeights = tuple(probs[prevSubstr][c] for c in chars)
        char = random.choices(chars, weights=charWeights)[0]
        if char == "_":
            break
        yield char
        prevSubstr = prevSubstr[1:] + char

def main():
    if len(sys.argv) != 3:
        sys.exit(
            "Argument: FILE ORDER (FILE = file to read strings from, ORDER = "
            "order of Markov chain (1-5))"
        )
    (inputFile, order) = sys.argv[1:]
    if not os.path.isfile(inputFile):
        sys.exit("Input file not found.")
    try:
        order = int(order)
        if not 1 <= order <= 5:
            raise ValueError
    except ValueError:
        sys.exit("Order of Markov chain must be 1-5.")

    origStrs = list(get_orig_strings(inputFile, order))
    probs = get_probs(origStrs, order)

    if DEBUG_MODE:
        for prev in sorted(probs):
            print(f'"{prev}": ' + ", ".join(
                (f"{probs[prev][char]}*" if probs[prev][char] > 1 else "")
                + ('" "' if char == " " else char)
                for char in sorted(probs[prev])
            ))
    else:
        results = set()
        while len(results) < RANDOM_COUNT:
            randomStr = "".join(get_random_string(probs))
            if len(randomStr) >= MIN_RANDOM_LENGTH \
            and (not IGNORE_ORIG or randomStr not in origStrs):
                results.add(randomStr)
        for result in sorted(results):
            print(result)

main()
