class Screen:
    def __init__(self, width):
        self.col = 0
        self.x = 1
        self.width = width
        self.display_row = ''

    def tick(self):
        self.display_row += '#' if abs(self.x-self.col)<=1 else '.'
        self.col += 1
        if self.col == self.width:
            print(self.display_row)
            self.display_row = ''
            self.col = 0

    def addx(self, to_add):
        self.x += int(to_add)

def main():
    Crt = Screen(40)
    
    with open('program.txt') as document:
        for line in document:
            line = line.strip('\n')
            Crt.tick()
            if line != 'noop':
                instr, n = line.split(' ')
                Crt.tick()
                Crt.addx(n)
                
if __name__ == "__main__":
    main()