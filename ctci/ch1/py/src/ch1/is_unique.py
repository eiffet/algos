
# using set to track chars
# O(n) time, O(n) space

def has_unique_chars(s):
    unique_set = set()
    for i in xrange(len(s)):
        if s[i] in unique_set:
            return False
        unique_set.add(s[i])
    return True


# without additional data structures
# O(nlogn) time, O(1) space

def has_unique_chars_inplace(s):
    s = sorted(s)
    if len(s) <= 1:
        return True
    prev = s[0]
    for i in xrange(1, len(s)):
        if s[i] == prev:
            return False
        prev = s[i]
    return True
