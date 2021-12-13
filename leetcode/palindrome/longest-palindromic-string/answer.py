from typing import List


my_str = 'ccabadd'

def longest_palindrome(my_str: str) -> str:
    if not my_str or len(my_str) < 1:
        return ""

    start, end = 0
    for i in range(len(my_str)):
        len1 = expand_around_center(my_str, i, i) #2
        len2 = expand_around_center(my_str, i, i+1) #0
        len = max(len1, len2)

        if len > (end - start):
            start = i - (len - 1) / 2
            end = i + len / 2

    return my_str[start:end+1]

def expand_around_center(s: str, left: int, right: int) -> int:
    L=left, R=right
    # i=1, L = 1, R = 2, s[L] = 'c', s[R] = 'a'
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L - 1

