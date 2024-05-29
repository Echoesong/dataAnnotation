import re

with open("coding_qual_input.txt", "r") as file:
    cipher = {}
    pattern = r"\d"
    for line in file:
        digits = []
        alphabet = []
        middle = 0
        for i, character in enumerate(line):
            # Check if it's a number. If it is, append it to digits; if it's not, we've found the middle and set middle to i
            if re.fullmatch(pattern, character):
                digits.append(character)
            else:
                middle = i
                break
        for j, character in enumerate(line):
            if j > middle:
                alphabet.append(character)
        finalDigits = int("".join(digits))
        finalAlphabet = "".join(alphabet).strip()
        cipher[finalDigits] = finalAlphabet

    # Below is setting up the pyramid
    encodedDigits = sorted(cipher.keys())
    digitsLength = len(encodedDigits)
    incrementer = 0
    countToAdd = incrementer + 1
    pyramid = []
    while incrementer < digitsLength:
        row = []
        for n in range(countToAdd):
            if len(encodedDigits) == 0:
                break
            popped = encodedDigits.pop(0)
            row.append(popped)
        incrementer += 1
        countToAdd = incrementer + 1
        pyramid.append(row)
    output = []
    for array in pyramid:
        if array:
            toPopIn = array.pop()
            output.append(toPopIn)
    answers = [
        cipher[answerNumber] for answerNumber in output if answerNumber in cipher
    ]
    returnValue = " ".join(answers)
    print(returnValue)

# I think I want to flag 'good digits'
# So I need to write a function that will output
