file = open('..\\Puzzle 1\\input.txt')

def find_repeat(str_1, str_2, str_3):
    cache = {}

    for char in str_1:
        if char not in cache:
            cache[char] = 1

    for char in str_2:
        if char in cache:
            cache[char] = 2

    for char in str_3:
        if char in cache:
            if cache[char] == 2:
                return char


def badge_sum(handle):
    total = 0
    group = [None] * 3

    for line in handle:
        line = line.rstrip()

        if group[0] is None:
            group[0] = line
        elif group[1] is None:
            group[1] = line
        elif group[2] is None:
            group[2] = line

        if group[0] and group[1] and group[2]:
            char_code = ord(find_repeat(group[0], group[1], group[2]))

            if 64 < char_code < 91:
                total += char_code - 38
            else:
                total += char_code - 96
            group = [None] * 3

    return total


print(badge_sum(file))
