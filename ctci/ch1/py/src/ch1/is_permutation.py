
# check if one string is a permutation of another
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    char_counts = dict()
    for i in xrange(len(str1)):
        if str1[i] not in char_counts:
            char_counts[str1[i]] = 0
        char_counts[str1[i]] += 1
    for j in xrange(len(str2)):
        if str2[j] not in char_counts:
            return False
        char_counts[str2[j]] -= 1
    for v in char_counts.itervalues():
        if v != 0:
            return False
    return True
