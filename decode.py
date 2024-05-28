lines = []

with open("coding_qual_input.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

print(lines)
