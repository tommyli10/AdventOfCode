file = open('input.txt')

def count_char(handle):
    line = handle.readline()
    start = 0
    while start + 4 < len(line):
        substr = line[start: start + 4]
        if len(set(substr)) != len(substr):
            start += 1
        else:
            return start + 4


print(count_char(file))

# str = 'abcdefg'
# print(str[1:5]) # bcde