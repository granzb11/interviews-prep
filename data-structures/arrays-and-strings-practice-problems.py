"""1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?"""

def is_unique(str) -> bool:
    """Implementation without any data structures"""
    for i in range(0, len(str)):
        #if first letter
        if i == 0:
            new_str = str[1:]
        #if last letter
        elif i == len(str) - 1:
            new_str = str[:i-1]
        else:
            new_str = str[:i-1] + str[i+1:]

        if str[i] in new_str:
            return False

    return True

def is_unique_with_list(str) -> bool:
    for i in range(0, len(str)):
        str_list = list(str)
        my_char = str_list.pop(i)
        if my_char in str_list:
            return False
    return True

def is_unique_bit_manipulation(str):
    checker: int = 0
    for i in range(0, len(str)):
        my_char = str[i]
        my_char_binary: int = ord(my_char) - 97
        if checker & (1 << my_char_binary) > 0:
            return False
        else:
            checker = checker | (1 << my_char_binary)

    return True


""""""

def main():
    """1.1"""
    # print(f"Should return True: {is_unique('abcde')}")
    # print(f"Should retrun False: {is_unique('abcdd')}")
    # print(f"Should return True: {is_unique_with_list('abcde')}")
    # print(f"Should retrun False: {is_unique_with_list('abcdd')}")
    # print(f"Should return True: {is_unique_bit_manipulation('abcde')}")
    # print(f"Should retrun False: {is_unique_bit_manipulation('abcdd')}")


if __name__ == '__main__':
    main()