def main():
    trees = []
    visible = []
    with open('trees.txt') as document:
        for line in document:
            row = []
            mark_row = []
            for char in line:
                row.append(int(char))
                mark_row.append(0)
            trees.append(row)
            visible.append(mark_row)

    # Initialize table marking visibility:
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
    h = len(trees)
    w = len(trees[0])
    top = []
    bot = []
    left = []
    right = []
    for i in range(h):
        top_curr = []
        bot_curr = []
        left_curr = []
        right_curr = []
        for j in range(w):
            top_curr.append(0)
            bot_curr.append(0)
            left_curr.append(0)
            right_curr.append(0)
        top.append(top_curr)
        bot.append(bot_curr)
        left.append(left_curr)
        right.append(right_curr)


    # Loop through to count trees that are visible from each direction
    for i in range(1,h-1):
        for j in range(1,w-1):
            top[i][j] = max(trees[i-1][j], top[i-1][j])
            if trees[i][j] > top[i][j]:
                visible[i][j] = 1
            bot[h-1-i][j] = max(trees[h-i][j], bot[h-i][j])
            if trees[h-i-1][j] > bot[h-i-1][j]:
                visible[h-i-1][j] = 1
            left[i][j] = max(trees[i][j-1], left[i][j-1])
            if trees[i][j] > left[i][j]:
                visible[i][j] = 1
            right[i][w-1-j] = max(trees[i][w-j], right[i][w-j])
            if trees[i][w-1-j] > right[i][w-1-j]:
                visible[i][w-1-j] = 1

    # Count trees marked as visible
    count = 0
    for row in visible:
        for item in row:
            count += item
    print(count)
                
if __name__ == "__main__":
    main()