'''https://leetcode.com/problems/scramble-string/'''

import sys


def sol(s1, s2) -> bool:
    if len(s1) != len(s2):
        return False
    if set(s1) != set(s2):
        return False
    if len(s1) <= 3:
        return s1 == s2 or s1 == s2[::-1]
    else:
        mid = len(s1) // 2
        # print(mid)
        # sys.stderr.write(str(mid))
        return sol(s1[:mid], s2[:mid]) and sol(s1[mid:], s2[mid:])


if __name__ == "__main__":
    s1 = 'abb'
    s2 = 'bab'
    print(sol(s1, s2))
