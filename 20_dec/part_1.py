from itertools import product
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed

def get_input(filename):
    with open(filename, 'r') as file:
        walls, road, start, end = set(), set(), None, None
        grid = [line for line in file.read().strip().split('\n')]
        for x, y in product(range(len(grid)), range(len(grid))):
            match grid[x][y]:
                case '#': walls.add((x, y))
                case '.': road.add((x, y))
                case 'S': start = (x, y)
                case 'E': 
                    end = (x, y)
                    road.add(end)
        return walls, road, start, end

def get_next(pos, road):
    x, y = pos
    for d in [(1,0),(0,1),(-1,0),(0,-1)]:
        if (x + d[0], y + d[1]) in road: 
            road.remove((x + d[0], y + d[1]))
            return (x + d[0], y + d[1])

def find_path(road, start, end):
    path, dist = [start], {start: 0}
    curr = start
    while curr != end:
        next = get_next(curr, road)
        path += [next]
        dist[next] = dist[curr] + 1
        curr = next
    return path, dist

def find_valid_cheats(walls, path, dist, end):
    opts = [(2,0),(0,2),(-2,0),(0,-2)]
    valid_cheats = 0
    to_end = dist[end]
    for x, y in path:
        curr_dist = dist[(x, y)]
        for dx, dy in opts:
            test = x + dx, y + dy
            wall = x + (dx//2), y + (dy//2)
            if test not in dist or wall not in walls: continue
            t_dist = to_end - dist[test]
            if (to_end - t_dist) - (curr_dist + 2) >= 100:
                valid_cheats += 1
    return valid_cheats

@timed
def main():
    walls, road, start, end = get_input('./input.txt')
    path, dist = find_path(road, start, end)
    print(find_valid_cheats(walls, path, dist, end))

if __name__ == "__main__":
    main()
