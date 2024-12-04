import re

input_file = open("input.txt").read()


# Searches for multiplay functions in the code
def find_muls(text):
    total_muls = []
    current_mul = ""
    for letter in text:
        if current_mul == "":
            if letter == "m":
                current_mul += "m"     
        elif current_mul == "m":
            if letter == "u":
                current_mul += "u"
            else:
                current_mul = ""
        elif current_mul == "mu":
            if letter == "l":
                current_mul += "l"
            else:
                current_mul = ""
        elif current_mul == "mul":
            if letter == "(":
                current_mul += "("
            else:
                current_mul = ""
        elif current_mul == "mul(":
            if re.search(r"[\d]", letter):
                current_mul += letter
            else:
                current_mul = ""
        elif re.fullmatch(r"mul\([\d]+", current_mul):
            if re.search(r"[\d]", letter):
                current_mul += letter
            elif letter == ",":
                current_mul += letter
            else:
                current_mul = ""
        elif re.fullmatch(r"mul\([\d]+,", current_mul):
            if re.search(r"[\d]", letter):
                current_mul += letter
            else:
                current_mul = ""
        elif re.fullmatch(r"mul\([\d]+,[\d]+", current_mul):
            if re.search(r"[\d]", letter):
                current_mul += letter
            elif letter == ")":
                current_mul += letter
                total_muls.append(current_mul)
                current_mul = ""
            else:
                current_mul = ""

    return total_muls


# Multiples a mul function
def do_mul(string):
    reached_comma = False
    first = ""
    second = ""
    for letter in string:
        if re.search(r"[\d]", letter):
            if reached_comma == False:
                first += letter
            else:
                second += letter
        elif letter == ",":
            reached_comma = True
        elif letter == ")":
            break
    
    return int(first) * int(second)


# Main Program
muls = find_muls(input_file)
total = 0
for mul in muls:
    total += do_mul(mul)
print(total)