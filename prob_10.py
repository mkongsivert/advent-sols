def main():
    time = 0
    x = 1
    measured = [20, 60, 100, 140, 180, 220]
    measurements = []
    
    with open('program.txt') as document:
        for line in document:
            line = line.strip('\n')
            time += 1
            if time == measured[0]:
                measurements.append(time*x)
                measured = measured[1:]
            if measured == []:
                break
            if line != 'noop':
                instr, n = line.split(' ')
                time += 1
                if time == measured[0]:
                    measurements.append(time*x)
                    measured = measured[1:]
                if measured == []:
                    break
                x += int(n)
    print(sum(measurements))
                
if __name__ == "__main__":
    main()