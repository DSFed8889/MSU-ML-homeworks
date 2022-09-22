import re


def find_shortest(s):
    return len(min(re.findall('[a-z|A-Z]+', s), key=len, default=''))
