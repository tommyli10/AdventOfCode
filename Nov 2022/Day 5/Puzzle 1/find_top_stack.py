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

    for l in crate_list:
        print(crate_list[l])

    # iterate through instructions
    line = handle.readline()
    line = handle.readline()


    return output

print(find_top_stack(file))