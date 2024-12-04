input_file = open("/Users/michael/repos/advent24/4/input.txt").read()


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
            if y == "X":
                coordinates_list.append([y_count, x_count])
            
            y_count += 1
        
        x_count += 1

    return coordinates_list


# For each coordinate, look for matches 
def get_matches(coordinates, processed_file):
    matches = 0
    y, x = coordinates
    if not x < 3:
        if processed_file[x-1][y] == "M" and processed_file[x-2][y] == "A" and processed_file[x-3][y] == "S":
            matches += 1
    
    if not x < 3 and not y < 3:
        if processed_file[x-1][y-1] == "M" and processed_file[x-2][y-2] == "A" and processed_file[x-3][y-3] == "S":
            matches += 1

    if not y < 3:
        if processed_file[x][y-1] == "M" and processed_file[x][y-2] == "A" and processed_file[x][y-3] == "S":
            matches += 1

    if not x > 136 and not y < 3:
        if processed_file[x+1][y-1] == "M" and processed_file[x+2][y-2] == "A" and processed_file[x+3][y-3] == "S":
            matches += 1

    if not x > 136:
        if processed_file[x+1][y] == "M" and processed_file[x+2][y] == "A" and processed_file[x+3][y] == "S":
            matches += 1
    
    if not x > 136 and not y > 136:
        try:
            if processed_file[x+1][y+1] == "M" and processed_file[x+2][y+2] == "A" and processed_file[x+3][y+3] == "S":
                matches += 1
        except:
            print(x, y)

    if not y > 136:
        if processed_file[x][y+1] == "M" and processed_file[x][y+2] == "A" and processed_file[x][y+3] == "S":
            matches += 1
    
    if not x < 3 and not y > 136:
        if processed_file[x-1][y+1] == "M" and processed_file[x-2][y+2] == "A" and processed_file[x-3][y+3] == "S":
            matches += 1
    
    return matches


# Main Program
organised = organise(input_file)
total = 0
all = find_xs(organised)
for match in all:
    total += get_matches(match, organised)

print(total)