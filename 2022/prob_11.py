class Monkey:
    def __init__(self, start_items, oper, test, if_true, if_false):
        self.items = []
        for item in start_items.split(', '):
            self.items.append(int(item))
        self.oper = oper
        self.test = int(test)
        self.t = int(if_true)
        self.f = int(if_false)
        self.business = 0

    def operation(self, x):
        operator, operand = self.oper.split(' ')
        if operator == '+':
            return x*2 if operand == 'old' else x+int(operand)
        elif operator == '*':
            return x**2 if operand == 'old' else x*int(operand)
        else:
            print('Not a recognized operator')
            return None
        
    def turn(self):
        item = self.items.pop(0)
        item = self.operation(item) # Inspection
        #item = item // 3 # Getting bored
        self.business += 1
        return (item, self.t) if item % self.test == 0 else (item, self.f)
        
def main():
    monkeys = []
    monk_start_items, monk_oper, monk_test, monk_t, monk_f = '','','','',''
    # Read in monkeys
    with open('monkeytest.txt') as document:
        while True:
            line = document.readline()
            if not line:
                break
            if line[0:7] != 'Monkey ':
                print('Reading error')
                return None
            monk_start_items = document.readline().strip('  Starting items: ').strip('\n')
            monk_oper = document.readline().strip('  Operation: new = old ').strip('\n')
            monk_test = document.readline().strip('  Test: divisible by ').strip('\n')
            monk_t = document.readline().strip('\n')[-1]
            monk_f = document.readline().strip('\n')[-1]
            monkeys.append(Monkey(monk_start_items, monk_oper, monk_test, monk_t, monk_f))
            line = document.readline()
            if not line:
                break

    # Run rounds
    for i in range(10000):
        if i%500==0:
            print(i)
        for monk in monkeys:
            while monk.items != []:
                moved_item, to = monk.turn()
                monkeys[to].items.append(moved_item)

    # Calculate monkey business
    for i in range(len(monkeys)):
        print('Monkey '+str(i)+' inspected items '+str(monkeys[i].business)+' times.')


if __name__ == "__main__":
    main()