input_file = open("/Users/michael/repos/advent24/2/input.txt").read()


# Splits file into lists of reports with sublists for levels
def organise_reports(file):
    output = []

    for report in file.split('\n'):
        temp_output = []

        for level in report.split(' '):
            if level == '\n' or level == ' ':
                continue

            temp_output.append(int(level))
        
        if temp_output == []:
            continue

        output.append(temp_output)
    
    return output


# Checks if levels are all increasing/decreasing
# Returns True if all increasing/decreasing, False if not all increasing/decreasing
def levels_all_increasing_or_decreasing(report):
    # 1 = increasing, 0 = decreasing
    if report[0] > report[1]:
        status = 0
    elif report[1] > report[0]:
        status = 1
    else:
        return False
    
    previous_level = report[0]
    done_first_report = False

    for level in report:
        if done_first_report == False:
            done_first_report = True
            continue

        if status == 0:
            if level > previous_level:
                return False
        elif status == 1:
            if previous_level > level:
                return False
            
        if previous_level == level:
            return False
        
        previous_level = level
    
    return True


# Checks if reports increase/decrease by less than 4
def levels_increase_less_than_4(report):
    previous_level = report[0]
    done_first_report = False

    for level in report:
        if done_first_report == False:
            done_first_report = True
            continue

        if abs(int(level) - int(previous_level)) > 3:
            return False
        previous_level = level
    return True


# Try removing each level and see if any work
def try_remove_levels(report):
    for x in range(0, report.__len__()):
        report_copy = report.copy()
        report_copy.pop(x)
        if levels_all_increasing_or_decreasing(report_copy) + levels_increase_less_than_4(report_copy) == 2:
            return True
    
    return False


# Main Program
reports = organise_reports(input_file)
total_safe = 0
for report in reports:
    if try_remove_levels(report):
        total_safe = total_safe + 1

print(total_safe)