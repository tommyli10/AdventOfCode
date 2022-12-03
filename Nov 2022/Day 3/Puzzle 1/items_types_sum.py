file = open('input.txt')

# print(ord('A')) # 65
# print(ord('Z')) # 90

# print(ord('a')) # 97
# print(ord('z')) # 122

def find_dup(str_1, str_2):
    cache = {}

    for char in str_1:
        if char in cache:
            cache[char] += 1
        else:
            cache[char] = 1

    for char in str_2:
        if char in cache:
            return char


def items_types_sum(handle):
    total = 0

    for line in handle:
        line = line.rstrip()
        first_half = line[:len(line) // 2]
        second_half = line[len(line) // 2:]

        dup_char = find_dup(first_half, second_half)
        char_code = ord(dup_char)

        if 64 < char_code < 91:
            total += char_code - 38
        else:
            total += char_code - 96

    return total

print(items_types_sum(file))