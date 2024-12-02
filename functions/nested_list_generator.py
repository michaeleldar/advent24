# Splits string into single nested lists.
# Inputs: string, major deliminator, minor diliminator, if the values should be ints

def organise_reports(file, major, minor, is_int):
    output = []

    for report in file.split(major):
        temp_output = []

        for level in report.split(minor):
            if level == '\n' or level == ' ':
                continue

            if is_int:
                temp_output.append(int(level))
            else:
                temp_output.append(level)
        
        if temp_output == []:
            continue

        output.append(temp_output)
    
    return output