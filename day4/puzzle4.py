import numpy as np
PROP1 = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"].sort()
PROP2 = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].sort()

def read_input():
    counter = 0
    with open("day4/input4.txt", "r") as f: 
        raw_passport = []
        while line := f.readline():
            if line != "\n":
                raw_passport.append(line.rstrip())
            else:
                counter += process_passport(raw_passport)
                raw_passport = []
    return counter + 1

def process_passport(raw_passport):
    passport = []
    for line in raw_passport:
        passport += line.split(" ")
    properties = []
    for prop in passport:
        properties.append(prop.split(":")[0])
    if len(properties) < 7:
        return 0
    if len(properties) == 7 and properties.sort() == PROP2:
        return 1
    if len(properties) == 8 and properties.sort() == PROP1:
        return 1


print(read_input())
