file = open('input.txt')

def count_char_two(handle):
    line = handle.readline()
    start = 0
    while start + 14 < len(line):
        substr = line[start: start + 14]
        if len(set(substr)) != len(substr):
            start += 1
        else:
            return start + 14

print(count_char_two(file))