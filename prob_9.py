def make_2d_list(height, width):
    output = []
    for i in range(height):
        curr = []
        for j in range(width):
            curr.append(0)
        output.append(curr)
    return output

def size_board():
    with open('rope_path.txt') as document:
        # Read through once to get the size of the board
        v_max, v_min, h_max, h_min = 0,0,0,0
        v_curr, h_curr = 0,0
        for line in document:
            direction, dist = line.strip('\n').split(' ')
            if direction == 'U':
                v_curr -= int(dist)
                v_min = min(v_min, v_curr)
            elif direction == 'D':
                v_curr += int(dist)
                v_max = max(v_max, v_curr)
            elif direction == 'L':
                h_curr -= int(dist)
                h_min = min(h_min, h_curr)
            elif direction == 'R':
                h_curr += int(dist)
                h_max = max(h_max, h_curr)
        return (v_max, v_min, h_max, h_min)

def main():
    v_max, v_min, h_max, h_min = size_board()
    board = make_2d_list(v_max-v_min, h_max-h_min)
    H = [v_max, (-h_min)]
    T = [v_max, (-h_min)]
    board[v_max][h_min] = 1
    with open('rope_path.txt') as document:
        # Let the path play out
        for line in document:
            direction, dist = line.strip('\n').split(' ')
            if direction == 'U':
                for i in range(int(dist)):
                    H[0] -= 1
                    if abs(H[0]-T[0]) == 2:
                        T[0] = T[0] - 1 # vertical pull
                        T[1] = H[1] # diagonal pull
                        board[T[0]][T[1]] = 1
            elif direction == 'D':
                for i in range(int(dist)):
                    H[0] += 1
                    if abs(H[0]-T[0]) == 2:
                        T[0] += 1 # vertical pull
                        T[1] = H[1] # diagonal pull
                        board[T[0]][T[1]] = 1
            elif direction == 'L':
                for i in range(int(dist)):
                    H[1] -= 1
                    if abs(H[1]-T[1]) == 2:
                        T[1] -= 1 # horizontal pull
                        T[0] = H[0] # diagonal pull
                        board[T[0]][T[1]] = 1
            elif direction == 'R':
                for i in range(int(dist)):
                    H[1] += 1
                    if abs(H[1]-T[1]) == 2:
                        T[1] += 1 # horizontal pull
                        T[0] = H[0] # diagonal pull
                        board[T[0]][T[1]] = 1
    # Count marked points
    marked = 0
    for i in range(v_max - v_min):
        for j in range(h_max - h_min):
            marked += board[i][j]
    print(marked)

                
if __name__ == "__main__":
    main()