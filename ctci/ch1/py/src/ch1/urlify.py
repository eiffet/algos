
# replace all spaces in a string with '%20'
# assume sufficient space at the end of the string to hold the additional characters,
# and you are given the "true" length of the string

def urlify(s, length):
    result = list()
    for i in xrange(length):
        if s[i] == ' ':
            result.append('%20')
        else:
            result.append(s[i])
    return str.join('', result)


def urlify_in_place(s, length):
    last_index = length - 1
    index = 0
    while index < len(s):
        c = s[index]
        if c == ' ':
            for i in xrange(last_index, index, -1):
                s[i+2] = s[i]
            s[index] = '%'
            s[index+1] = '2'
            s[index+2] = '0'
            last_index += 2
            index += 2
        else:
            s[index] = c
            index += 1
    return str.join('', s)

print urlify('Mr John Smith    ', 13)
print urlify_in_place(list('Mr John Smith    '), 13)
