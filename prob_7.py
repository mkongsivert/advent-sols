import sys

class Tree:
    def __init__(self, val, par=None):
        self.key = val
        self.files_size = 0
        self.total_size = 0
        self.children = []
        self.parent = par

def sum_small_files(Root):
    leaf_total = 0
    leaf_total += Root.total_size if Root.total_size <= 100000 else 0
    for child in Root.children:
            leaf_total += sum_small_files(child)
    return leaf_total

def update_size(Root):
    tree_total = Root.files_size
    for child in Root.children:
        update_size(child)
        tree_total += child.total_size
    Root.total_size = tree_total

def main():
    # Build the file tree:
    Files = None
    current = None
    with open('directories.txt') as document:
        for line in document:
        # for itr in range(70):
        #     line = document.readline()
            line = line.strip('\n')
            if line[0] == '$':
                line = line[2:] # strip $
                if line[0:2] == 'cd':
                    line = line[3:] # strip cd command
                    if line == '/':
                        Files = Tree('/')
                        current = Files
                    elif line == '..':
                        current = current.parent
                    else:
                        for child in current.children:
                            if type(child) == Tree and child.key == line:
                                current = child
                                break
                elif line[0:2] == 'ls':
                    if current.children != []:
                        print(current.children)
                    pass # display contents
            elif line[0].isnumeric():
                filesize = line.split(' ')[0]
                current.files_size += int(filesize)
            elif line[0:3] == 'dir':
                dir_name = line.split(' ')[1]
                current.children.append(Tree(dir_name, current))

    # Add up all subdirectory sizes:
    update_size(Files)
    space_needed = 30000000 - (70000000 - Files.total_size)
    print('Space needed: '+str(space_needed))
    # Read the file tree (DFS):
    Queue = [Files]
    smallest_large_file = sys.maxsize
    while Queue != []:
        curr = Queue[0]
        Queue = Queue[1:] + curr.children
        if curr.total_size >= space_needed and curr.total_size < smallest_large_file:
            smallest_large_file = curr.total_size
    print(smallest_large_file)

if __name__ == "__main__":
    main()