file = open('input.txt')

def find_top_stack(handle):
    output = ''
    crate_list = {}
    line = handle.readline()
    for i in range(int(len(line) / 4)):
        crate_list[i + 1] = []

    # get lists of crates
    while True:
        line = line.rstrip()
        try:
            int(line[1])
            break
        except:
            i = 1
            # print(max(crate_list, key=int))
            while i <= max(crate_list, key=int):
                char_index = (i - 1) * 4 + 1
                if len(line) >= char_index and line[char_index] != ' ':
                    crate_list[i].append(line[char_index])
                i += 1
            line = handle.readline()

    # iterate through instructions
    line = handle.readline()
    line = handle.readline().rstrip()
    while len(line):
        steps = line.split()
        list_to_move = list(reversed(crate_list[int(steps[3])][:int(steps[1])]))
        crate_list[int(steps[5])] = list_to_move + crate_list[int(steps[5])]
        crate_list[int(steps[3])] = crate_list[int(steps[3])][int(steps[1]):]
        line = handle.readline().rstrip()

    for section in crate_list:
        output += crate_list[section][0]
    return output

print(find_top_stack(file))

# l2 = [1,2,3,4,5]
# print(l2[:3]) # [1,2,3]

# l2 = [1,2,3,4,5]
# print(l2[3:]) # [4,5]