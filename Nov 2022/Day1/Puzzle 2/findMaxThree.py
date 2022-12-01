file = open('input.txt')


def find_max_three(handle):
    total = 0
    totals = []
    temp_total = 0

    for line in handle:
        if line != '\n':
            line = line.rstrip()
            temp_total += int(line)
        else:
            totals.append(temp_total)
            temp_total = 0

    totals.sort(reverse=True)

    return sum(totals[:3])


print(find_max_three(file))
