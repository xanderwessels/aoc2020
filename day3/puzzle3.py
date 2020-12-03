def read_input():
    with open("day3/input3.txt", "r") as f: 
        return [[c for c in line][0:-1] for line in f.readlines()]

def count_trees(right, down, inp):
    x = 0
    y = 0
    grid = inp
    trees = 0
    while y < len(grid):
        if grid[y][x] == '#':
            trees = trees+1
        y=(y+down)
        x=(x+right) % len(grid[0])
        print(y)
    return trees

def part1():
    print(count_trees(3,1,read_input()))

def part2():
    print( count_trees(1,1,read_input()) * \
            count_trees(3,1,read_input()) * \
            count_trees(5,1,read_input()) * \
            count_trees(7,1,read_input()) * \
            count_trees(1,2,read_input()) )

part2()