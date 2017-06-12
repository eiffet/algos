
# check if a string is a permutation of a palindrome.
# spaces might be in the string


def has_palindrome(s):
    if len(s) < 2:
        return True
    char_counts = dict()
    for i in xrange(len(s)):
        if s[i] in [' ', '\t', '\n']:
            continue
        if s[i] not in char_counts:
            char_counts[s[i]] = 0
        char_counts[s[i]] += 1
    odd_count = 0
    for v in char_counts.itervalues():
        if v % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    return True

print has_palindrome('taco cat')
print has_palindrome('')
print has_palindrome('a')
print has_palindrome('123456')
