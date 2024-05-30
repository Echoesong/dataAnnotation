import re


def parse_file(file_name):
    cipher = {}
    pattern = r"\d"
    with open(file_name, "r") as file:
        for line in file:
            digits = []
            alphabet = []
            middle = 0
            for i, character in enumerate(line):
                if re.fullmatch(pattern, character):
                    digits.append(character)
                else:
                    middle = i
                    break
            alphabet = line[middle:].strip()
            finalDigits = int("".join(digits))
            cipher[finalDigits] = alphabet
    return cipher


def build_pyramid(encoded_digits):
    encoded_digits_sorted = sorted(encoded_digits)
    index = 0
    count_to_add = index + 1
    pyramid = []

    while encoded_digits_sorted:
        row = [
            encoded_digits_sorted.pop(0)
            for _ in range(count_to_add)
            if encoded_digits_sorted
        ]
        pyramid.append(row)
        index += 1
        count_to_add = index + 1

    return pyramid


def decode_pyramid(pyramid, cipher):
    output = [array.pop() for array in pyramid if array]
    answers = [
        cipher[answerNumber] for answerNumber in output if answerNumber in cipher
    ]
    return " ".join(answers)


def decode():
    cipher = parse_file("coding_qual_input.txt")
    pyramid = build_pyramid(cipher.keys())
    return decode_pyramid(pyramid, cipher)


print(decode())
