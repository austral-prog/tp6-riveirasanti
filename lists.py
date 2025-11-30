def remove_elements(list_to_remove_elements):
    result = []
    for i in range(len(list_to_remove_elements)):
        if i != 0 and i != 4 and i != 5:
            result.append(list_to_remove_elements[i])
    return result

def add_elements(list_to_add_elements):
    return ['Pink'] + list_to_add_elements + ['Yellow']

def is_empty(list_to_check):
    return len(list_to_check) == 0

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    return list_to_compare1[2] == list_to_compare2[2]

def list_of_lists(list_of_lists_to_modify):
    return [list_of_lists_to_modify[0][:2], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2][-2:]]