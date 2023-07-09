# generate random strings based on source data using a character-level Markov
# chain

import random, re, sys

# file to read original strings from; one per line;
# see readme for sources of these files
STRING_FILE = "england-cities,towns.txt"
#STRING_FILE = "finland-municipalities.txt"

# order of Markov chain (how many previous characters affect each new
# character); minimum = 1; maximum = length of shortest string in source data,
# plus one
MARKOV_ORDER = 3

# if 0, print random strings; if 1, print stats on source data
DEBUG_MODE = 0

# minimum length of random strings to print (if DEBUG=0)
MIN_RANDOM_LENGTH = 4

# ignore random strings that occur in original strings (0=no, 1=yes)
IGNORE_ORIG = 1

# how many random strings to print (if DEBUG=0)
RANDOM_COUNT = 50

def get_orig_strings():
    # generate original strings from file

    with open(STRING_FILE, "rt") as handle:
        handle.seek(0)
        for line in handle:
            stri = line.rstrip("\n")
            if len(stri) < MARKOV_ORDER - 1:
                print(
                    "Warning: skipping original string (too short): " + stri,
                    file=sys.stderr
                )
            if re.search(r"^[A-ZÅÄÖa-zåäö &'-]+$", stri) is None:
                sys.exit("Invalid characters in original string: " + stri)
            yield stri

def get_probs(origStrs):
    # origStrs: original strings (iterable)
    # return: probabilities (dict, see below)

    probs = {}  # {previous_character(s): {character: count, ...}, ...}

    for stri in origStrs:
        stri = "_" + stri + "_"  # "_" = start/end
        for i in range(MARKOV_ORDER, len(stri)):
            char = stri[i]
            prev = stri[i-MARKOV_ORDER:i]
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
    origStrs = list(get_orig_strings())
    probs = get_probs(origStrs)

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
