def dig_reader(S, i, j):
    digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    # check for spelled digits
    for dig in list(digits):
        if S[i:j].find(dig) > -1:
            return digits[dig]
    return ''

def prob_1():
    cal_sum = 0
    with open('cal_vals.txt') as document:
        for line in document:
            dig1, dig2 = None, 0
            n = len(line)
            for i in range(n):
                if line[i].isdigit():
                    dig1 = line[i]
                    break
                sp_digit = dig_reader(line, 0, i+1)
                if sp_digit:
                    dig1 = sp_digit
                    break
            for i in range(len(line))[::-1]:
                if line[i].isdigit():
                    dig2 = line[i]
                    break
                sp_digit = dig_reader(line, i, n)
                if sp_digit:
                    dig2 = sp_digit
                    break
            cal_sum += int(dig1+dig2)
    return cal_sum

def prob_2():
    pow_sum = 0
    with open('cube_games.txt') as document:
        for line in document:
            r_lim, g_lim, b_lim = 12, 13, 14
            r_max, g_max, b_max = 0,0,0
            ident, games = line.strip('\n').split(': ')
            ident = ident.strip('Game ')
            rounds = games.split('; ')
            for r in rounds:
                group = r.split(', ')
                for item in group:
                    num, color = item.split(' ')
                    if color == 'red':
                        r_max = max(r_max, int(num))
                    elif color == 'green':
                        g_max = max(g_max, int(num))
                    elif color == 'blue':
                        b_max = max(b_max, int(num))
                    else:
                        print('Unidentified color: '+color)
                        print(item)
            # if r_max <= r_lim and g_max <= g_lim and b_max <= b_lim:
            #     id_sum += int(ident)
            pow_sum += r_max*g_max*b_max
    return pow_sum

def prob_3():
    schem = []
    # Read in to make an interable
    with open('gondolas.txt') as document:
        for line in document:
            schem.append(line)
    pn = ''
    for i in range(len(schem)):
        for j in range(len(schem[i])):
            if schem[i][j].isdigit():
                pass
def main():
    print(prob_3())

if __name__ == "__main__":
    main()