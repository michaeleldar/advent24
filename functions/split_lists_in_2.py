# Takes an input of a list and a splitter and returns 2 lists,
# each item in the list containing one side of the string.

def split_lists(list, splitter):
    left_side = []
    right_side = []

    for item in list:
        left, right = item.split(splitter)
        left_side.append(left)
        right_side.append(right)
    
    return left_side, right_side