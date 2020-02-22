KNOWN_PHRASE = "the quick brown fox jumps over the lazy dog"
KNOWN_WORDS = KNOWN_PHRASE.split(' ')


# Create dict matching each letter from the line with the one from our known phrase
def find_decryption_dict(line: str):
    line_words = line.split(' ')
    if len(KNOWN_WORDS) == len(line_words):
        decryption_dict = dict()
        for known_word, line_word in zip(KNOWN_WORDS, line_words):
            if len(known_word) == len(line_word):
                for known_letter, line_letter in zip(known_word, line_word):
                    if line_letter in decryption_dict:
                        # If there was already a letter in the dict different to our known letter,
                        # then the line given doesn't match our known one (it should be consistent)
                        if decryption_dict[line_letter] != known_letter:
                            return None
                    else:
                        decryption_dict[line_letter] = known_letter
            else:
                return None
        return decryption_dict
    else:
        return None


def decrypt_line(line: str, decryption_dict: dict):
    decrypted_line = ""
    for character in line:
        if character in decryption_dict:
            decrypted_line += decryption_dict[character]
        else:
            decrypted_line += character
    return decrypted_line


test_cases = int(input())
input()

for test_case in range(test_cases):
    decryption_dict = None
    lines = list()
    line = input()
    try:
        while line:
            lines.append(line)
            if decryption_dict == None:
                decryption_dict = find_decryption_dict(line)
            line = input()
    except EOFError as err:
        pass

    if decryption_dict == None:
        print('No solution.')
    else:
        for line in lines:
            print(decrypt_line(line, decryption_dict))

    if test_case < test_cases - 1:
        print()  # Blank line between test cases (output)
