file = open('input.txt')

def find_overlap_pairs(handle):
    total = 0

    for line in handle:
        (group_1, group_2) = line.rstrip().split(',')
        (group_1_low, group_1_high) = group_1.split('-')
        (group_2_low, group_2_high) = group_2.split('-')

        if int(group_1_low) < int(group_2_low):
            if int(group_1_high) >= int(group_2_high):
                total += 1
        elif int(group_1_low) > int(group_2_low):
            if int(group_1_high) <= int(group_2_high):
                total += 1
        else:
            total += 1

    return total

print(find_overlap_pairs(file))