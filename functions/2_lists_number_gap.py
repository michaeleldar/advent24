# Works out the for every element combined in two lists. 
# Inputs are 2 lists and output is the total gap.
# Both lists must have the same amount of elements.

def find_side_gap(left_side, right_side):
    total_gap = 0

    for iteration in range(0, left_side.__len__()):
        total_gap = total_gap + abs(left_side[iteration] - right_side[iteration])

    return total_gap