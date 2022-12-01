file = open('input.txt')


def find_max_cal(handle):
    max_cal = 0
    temp_total = 0

    for line in handle:
        if line != '\n':
            line = line.rstrip()
            temp_total += int(line)
        else:
            if temp_total > max_cal:
                max_cal = temp_total
            temp_total = 0

    return max_cal


print(find_max_cal(file))
