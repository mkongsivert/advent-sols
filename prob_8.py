def make_2d_list(height, width):
    output = []
    for i in range(height):
        curr = []
        for j in range(width):
            curr.append(0)
        output.append(curr)
    return output

def count_visible_trees(tree_list):
    # Initialize table marking visibility:
    h = len(tree_list)
    w = len(tree_list[0])
    visible = []
    for i in range(h):
        mark_row = []
        for j in range(w):
            if i == 0 or j == 0:
                mark_row.append(1)
            elif i == h-1 or j == w-1:
                mark_row.append(1)
            else:
                mark_row.append(0)
        visible.append(mark_row)

    # Initialize four l-by-w 0 arrays
    top = make_2d_list(h, w)
    bot = make_2d_list(h, w)
    left = make_2d_list(h, w)
    right = make_2d_list(h, w)

    # Loop through to count trees that are visible from each direction (outside)
    for i in range(1,h-1):
        for j in range(1,w-1):
            top[i][j] = max(tree_list[i-1][j], top[i-1][j])
            if tree_list[i][j] > top[i][j]:
                visible[i][j] = 1
            bot[h-1-i][j] = max(tree_list[h-i][j], bot[h-i][j])
            if tree_list[h-i-1][j] > bot[h-i-1][j]:
                visible[h-i-1][j] = 1
            left[i][j] = max(tree_list[i][j-1], left[i][j-1])
            if tree_list[i][j] > left[i][j]:
                visible[i][j] = 1
            right[i][w-1-j] = max(tree_list[i][w-j], right[i][w-j])
            if tree_list[i][w-1-j] > right[i][w-1-j]:
                visible[i][w-1-j] = 1

    # Count trees marked as visible
    count = 0
    for row in visible:
        for item in row:
            count += item
    return count

def insert_tree(x, tree_row):
    return [x]+list(filter(lambda y: y>x, tree_row))

def compute_scenic_score(tree_list):
    # Initialize tables marking visible trees
    h = len(tree_list)
    w = len(tree_list[0])

    # Loop through to count trees that are visible from each direction (inside)
    max_scenic_score = 0
    for i in range(h):
        for j in range(w):
            x = i
            while x > 0:
                x -= 1
                if tree_list[x][j] >= tree_list[i][j]:
                    break
            up = i-x
            x = i
            while x<h-1:
                x += 1
                if tree_list[x][j] >= tree_list[i][j]:
                    break
            down = x-i
            x = j
            while x>0:
                x -= 1
                if tree_list[i][x] >= tree_list[i][j]:
                    break
            left = j-x
            x = j
            while x<w-1:
                x += 1
                if tree_list[i][x] >= tree_list[i][j]:
                    break
            right = x-j
            max_scenic_score = max(max_scenic_score, up*down*left*right)
    return max_scenic_score

testcase = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]

def main():
    trees = []
    with open('trees.txt') as document:
        for line in document:
            row = []
            line = line.strip('\n')
            for char in line:
                row.append(int(char))
            trees.append(row)

    print(compute_scenic_score(trees))

    
                
if __name__ == "__main__":
    main()