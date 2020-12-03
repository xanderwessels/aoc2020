def read_input():
    with open("day2/input2.txt", "r") as f: 
        i = []
        for line in f:
            (r, l, pw) = line.split(" ")
            (r1, r2) = r.split("-")
            i.append((int(r1), int(r2) , l[0], pw.rstrip()))
        return i

def part1():
    inp = read_input()
    total_count = 0
    for pws in inp:
        count = 0
        for ch in pws[3]:
            if ch == pws[2]:
                count = count + 1
        if count >= pws[0] and count <= pws[1]:
            total_count = total_count + 1
    print(total_count) 

def part2():
    inp = read_input()
    total_count = 0
    for pws in inp:
        count = 0
        if pws[3][pws[0]-1] == pws[2]:
            count = count + 1
        if pws[3][pws[1]-1] == pws[2]:
            count = count + 1
        if count == 1:
            total_count = total_count + 1
    print(total_count) 

part2()