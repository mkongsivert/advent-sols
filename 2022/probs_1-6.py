def prob_1():
    max_cals1 = 0
    max_cals2 = 0
    max_cals3 = 0
    elf_cals = 0
    with open('calories.txt') as inventory:
        for inv_line in inventory:
            item_cals = inv_line.strip('\n')
            if item_cals == '':
                if elf_cals > max_cals3:
                    max_cals3 = elf_cals
                    if max_cals3 > max_cals2:
                        max_cals3 = max_cals2
                        max_cals2 = elf_cals
                        if max_cals2 > max_cals1:
                            max_cals2 = max_cals1
                            max_cals1 = elf_cals
                elf_cals = 0
            else:
                elf_cals += int(item_cals)
    return max_cals1 + max_cals2 + max_cals3

def prob_2():
    match_score = {'X':0, 'Y':1, 'Z':2}
    shape_score = {'A': [3, 1, 2], 'B': [1, 2, 3], 'C': [2, 3, 1]}
    total_score = 0
    with open('rockpaperscissors.txt') as tournament:
        for round_line in tournament:
            op, me = round_line.strip('\n').split(' ')
            shape_id = match_score[me]
            total_score += 3*shape_id + shape_score[op][shape_id]
    return total_score

def prob_3():
    priority_sum = 0
    mod = 0
    with open('rucksacks.txt') as all_rucksacks:
        rucksack1 = ''
        rucksack2 = ''
        rucksack3 = ''
        for line in all_rucksacks:
            # gather into groups of three
            if mod == 0:
                rucksack1 = line.strip('\n')
                mod = 1
            elif mod == 1:
                rucksack2 = line.strip('\n')
                mod = 2
            elif mod == 2:
                rucksack3 = line.strip('\n')
                # find the repeated item:
                for let in rucksack1:
                    if let in rucksack2 and let in rucksack3:
                        # score the repeated item
                        priority_sum += (ord(let)-38) if let.isupper() else (ord(let)-96)
                        break
                mod = 0
    return priority_sum

def prob_4():
    contained = 0
    with open('section_assignment.txt') as document:
        for line in document:
            ass1, ass2 = line.strip('\n').split(',')
            start1, end1 = ass1.split('-')
            start2, end2 = ass2.split('-')
            if int(start1) < int(start2):
                contained += 0 if int(end1) < int(start2) else 1
            elif int(start2) < int(start1):
                contained += 0 if int(end2) < int(start1) else 1
            else:
                contained += 1
    return contained

def prob_5(s):
    with open('stack_ops.txt') as document:
        stacks = []
        for i in range(s):
            stacks.append([])
        while True:
            line = document.readline()
            if '[' not in line:
                document.readline() #extra blank line
                break
            for i in range(s):
                if line[4*i+1] != ' ':
                    stacks[i].append(line[4*i+1])
        while True:
            line = document.readline()
            if not line:
                break
            line = line.strip('\n').strip('move ')
            size, rest = line.split(' from ')
            fr, to = rest.split(' to ')
            n = int(size)
            x = int(fr)-1
            y = int(to)-1
            # STACK VERSION:
            # for i in range(int(n)):
            #     # pop from x
            #     let = stacks[int(x)-1].pop(0)
            #     # push to y
            #     stacks[int(y)-1].insert(0, let)
            mv = stacks[x][0:n]
            stacks[x] = stacks[x][n:]
            stacks[y] = mv + stacks[y]
        output = ''
        for i in range(s):
            if stacks[i] != []:
                output+=stacks[i][0]
        return output
    
def prob_6():
    with open('signal.txt') as document:
        signal = document.readline()
        last_fourteen = signal[0:14]
        for i in range(14, len(signal)):
            found = True
            for j in range(13):
                if last_fourteen[j] in last_fourteen[j+1:]:
                    found = False
            if found:
                return i
            else:
                last_fourteen = last_fourteen[1:] + signal[i]    


def main():
    print(prob_6())

if __name__ == "__main__":
    main()