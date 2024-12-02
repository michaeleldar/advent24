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


# Works out the gap between sides
def find_side_gap(left_side, right_side):
    total_gap = 0

    for iteration in range(0, left_side.__len__()):
        total_gap = total_gap + abs(left_side[iteration] - right_side[iteration])

    return total_gap

# Main Program
left_side, right_side = split_lists(input_file)
left_side = sorted(right_side)
right_side = sorted(right_side)
total_gap = find_side_gap(left_side, right_side)
print(total_gap)

# 21 Lines of code