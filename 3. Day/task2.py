import re
data = ""
file = open("input.txt", "r")
for list in file:
    data += list
file.close()

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, data)  

sum = 0
cond = 1
for string in matches:
    if string == "don't()":
        cond = 0
    elif string == "do()":
        cond = 1
    elif cond:
        regex = r"\d+"
        matches_new = re.findall(regex, string)
        sum += int(matches_new[0]) * int(matches_new[1])
        
print(sum)
