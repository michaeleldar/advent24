import re

input_file = open("/Users/michael/repos/advent24/3/input.txt").read()


# Searches for multiplay functions in the code
def find_muls(text):
    enabled = True
    total_muls = []
    current_mul = ""
    for letter in text:
        if current_mul == "":
            if letter == "m" and enabled == True:
                current_mul += "m"     
            elif letter == "d":
                current_mul += "d"
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
        elif current_mul == "d":
            if letter == "o":
                current_mul += "o"
            else:
                current_mul = ""
        elif current_mul == "do":
            if letter == "(":
                current_mul += "("
            elif letter == "n":
                current_mul += "n"
            else:
                current_mul = ""
        elif current_mul == "do(":
            if letter == ")":
                current_mul = ""
                enabled = True
            else:
                current_mul = ""
        elif current_mul == "don":
            if letter == "'":
                current_mul += "'"
            else:
                current_mul = ""
        elif current_mul == "don'":
            if letter == "t":
                current_mul += "t"
            else:
                current_mul = ""
        elif current_mul == "don't":
            if letter == "(":
                current_mul += "("
            else:
                current_mul = ""
        elif current_mul == "don't(":
            if letter == ")":
                current_mul = ""
                enabled = False
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