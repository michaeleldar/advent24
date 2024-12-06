# How to process rules. For every number in the update, if the rules say one of them should 
# be in front/behind it, the update list should follow this.


input_file = open("/Users/michael/repos/advent24/5/input.txt").read()


def organise_file(file):
    rules, order = file.split("#")
    rules_l = []
    orders_l = []

    for line in rules.split("\n"):
        if line == "":
            continue

        rules_l.append(line.split("|"))
    
    for line in order.split("\n"):
        orders_l.append(line.split(","))

    return rules_l, orders_l


def meets_prerequisites(page, rules, completed, non_completed):
    for rule in rules:
        if rule[0] == page:
            if rule[1] in completed:
                return False
        elif rule[1] == page:
            if rule[0] in non_completed:
                return False
    
    return True
    


def get_middle_value(update_list):
    return int(update_list[int((update_list.__len__() / 2) - 0.5)]) # -0.5 because lists start from 0


def eval_update_list(update_list, rules):
    completed = []
    non_completed = update_list.copy()

    for page in update_list:
        if meets_prerequisites(page, rules, completed, non_completed):
            completed.append(page)
            non_completed.pop(0)
        else:
            return 0
    
    return get_middle_value(update_list)


# Main Program
rules, orders = organise_file(input_file)
total = 0
for update_list in orders:
    if update_list == ['']:
        continue
    total += eval_update_list(update_list, rules)
print(total)