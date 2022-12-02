file = open('input.txt')

def calculate_score(handle):
    total_score = 0

    # X and A are rock, Y and B are paper, Z and C are scissors
    points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    for line in handle:
        [a, b] = line.rstrip().split()
        total_score += points[b]
        # calculate points from winning and tying
        if (a == 'A' and b == 'Y') or (a == 'B' and b == 'Z') or (a == 'C' and b == 'X'):
            total_score += 6
        elif (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z'):
            total_score += 3

    return total_score

print(calculate_score(file))