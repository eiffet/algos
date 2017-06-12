
# given 3 types of edits (insert char, remove char, replace char)
# and give 2 strings, check if they are one (or zero) edits away from each other


def is_one_away(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    a_index = 0
    b_index = 0
    missed = 0
    while a_index < len(a) and b_index < len(b):
        if a[a_index] != b[b_index]:
            if missed:
                return False
            missed += 1
            if len(a) > len(b):
                a_index += 1
            elif len(b) > len(a):
                b_index += 1
            else:
                a_index += 1
                b_index += 1
        else:
            a_index += 1
            b_index += 1
    return True

print is_one_away('brjad', 'brad')
print is_one_away('brad', 'brjd')
print is_one_away('bad', 'brad')
print is_one_away('bad', 'bsjd')
print is_one_away('bad', 'brad ')