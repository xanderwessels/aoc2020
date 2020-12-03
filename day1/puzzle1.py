import timeit
import functools

def read_input():
    with open("day1/input1.txt", "r") as f: 
        return [int(line.rstrip()) for line in f]

# Double for loop that checks every combination
def naive_part1():
    input = read_input()
    for i in input:
        for j in input:
            if i+j == 2020:
                return i*j

# Triple for loop that checks every combination
def naive_part2():
    input = read_input()
    for i in input:
        for j in input:
            for k in input:
                if i+j+k == 2020:
                    return i*j*k
                
instances = 100
t = timeit.Timer(functools.partial(naive_part1))
time1 = t.timeit(instances) / instances
print(time1)

instances = 100
t = timeit.Timer(functools.partial(naive_part2))
time1 = t.timeit(instances) / instances
print(time1)