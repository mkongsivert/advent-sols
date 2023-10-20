import sys

def reachable(a, b):
    if a == 'S':
        a = 'a'
    elif a == 'E':
        print('found')
        a = 'z'
    return abs(ord(a) - ord(b))<=1

def new_table(w, h, val):
    matrix = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(val)
        matrix.append(row)
    return matrix

def bfs(origin, graph):
    height = len(graph)
    width = len(graph[0])
    dist = new_table(width, height, sys.maxsize)
    dist[origin[0]][origin[1]] = 0
    queue = [origin]
    while queue != []:
        x, y = queue.pop(0)
        if graph[x][y] == 'E':
            return dist[x][y]
        # Check above
        if x>0 and reachable(graph[x][y], graph[x-1][y]):
            if dist[x-1][y] == sys.maxsize:
                queue.append([x-1, y])
                dist[x-1][y] = dist[x][y]+1
        # Check below
        if x<height-1 and reachable(graph[x][y], graph[x+1][y]):
            if dist[x+1][y] == sys.maxsize:
                queue.append([x+1, y])
                dist[x+1][y] = min(dist[x+1][y], dist[x][y]+1)
        # Check left
        if y>0 and reachable(graph[x][y], graph[x][y-1]):
            if dist[x][y-1] == sys.maxsize:
                queue.append([x, y-1])
                dist[x][y] = min(dist[x][y-1], dist[x][y]+1)
        # Check right
        if y<width-1 and reachable(graph[x][y], graph[x][y+1]):
            if dist[x][y+1] == sys.maxsize:
                queue.append([x, y+1])
                dist[x][y] = min(dist[x][y+1], dist[x][y]+1)

def main():
    hillmap = []
    start = None
    row = 0
    with open('pathtest.txt') as document:
        for line in document:
            if 'S' in line:
                start = [row, line.index('S')]
            hillmap.append(line.strip('\n'))
            row+=1
    
    return bfs(start, hillmap)

if __name__ == "__main__":
    main()