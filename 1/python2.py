input_file = open("input.txt").read()

# Splits into right and left sides
def split_lists(file):
    left_side = []
    right_side = []

    for line in file.split("\n"):
        if line == '':
            break

        left, right = line.split("   ")
        left_side.append(int(left)) 
        right_side.append(int(right))
    
    return left_side, right_side

# Look for matches for a certain number
def find_matches(number, right_side):
    match_score = 0
    for item in right_side:
        if item == number:
            match_score = match_score + number
    return match_score

# Main Program
left_side, right_side = split_lists(input_file)
match_score = 0
for item in left_side:
    match_score = match_score + find_matches(item, right_side)
print(match_score)