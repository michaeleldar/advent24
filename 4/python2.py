input_file = open("/Users/michael/repos/advent24/4/input copy.txt").read()


def organise(file):
    output = []

    for report in file.split("\n"):
        temp_output = []

        for level in list(report):
            if level == '\n' or level == ' ':
                continue
            
            temp_output.append(level)
        
        if temp_output == []:
            continue

        output.append(temp_output)
    
    return output


# Look for X's and return their "coordinates"
def find_xs(processed_file):
    x_count = 0
    coordinates_list = []
    for x in processed_file:
        y_count = 0
        for y in x:
            if y == "A":
                coordinates_list.append([y_count, x_count])
            
            y_count += 1
        
        x_count += 1

    return coordinates_list


# For each coordinate, look for matches 
def get_matches(coordinates, processed_file):
    amount_of_S = 0
    amount_of_M = 0
    y, x = coordinates
    if x == 0 or y == 0 or x == 139 or y == 139:
        return 0

    if processed_file[x-1][y-1] == "M":
        amount_of_M += 1
    elif processed_file[x-1][y-1] == "S":
        amount_of_S += 1
    else:
        return 0
    
    if processed_file[x+1][y-1] == "M":
        amount_of_M += 1
    elif processed_file[x+1][y-1] == "S":
        amount_of_S += 1
    else:
        return 0
    
    if processed_file[x-1][y+1] == "M":
        amount_of_M += 1
    elif processed_file[x-1][y+1] == "S":
        amount_of_S += 1
    else:
        return 0
    
    if processed_file[x+1][y+1] == "M":
        amount_of_M += 1
    elif processed_file[x+1][y+1] == "S":
        amount_of_S += 1
    else:
        return 0
    
    if amount_of_S > 2 or amount_of_M > 2:
        return 0
    else:
        return 1


# Main Program
organised = organise(input_file)
total = 0
all = find_xs(organised)
for match in all:
    total += get_matches(match, organised)

print(total)