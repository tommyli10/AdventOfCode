file = open('..\\Puzzle 1\\input.txt')

def re_calculate_score(handle):
    total_score = 0

    for line in handle:
        [a, b] = line.rstrip().split()
        # I have to lost if b is X
        if b == 'X':
            if a == 'A':
                total_score += 3
            elif a == 'B':
                total_score += 1
            else:
                total_score += 2
        # I have to tie if b is Y
        if b == 'Y':
            total_score += 3
            if a == 'A':
                total_score += 1
            elif a == 'B':
                total_score += 2
            else:
                total_score += 3
        # I have to win if b is Z
        if b == 'Z':
            total_score += 6
            if a == 'A':
                total_score += 2
            elif a == 'B':
                total_score += 3
            else:
                total_score += 1

    return total_score

print(re_calculate_score(file))