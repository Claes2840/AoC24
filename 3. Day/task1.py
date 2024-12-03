import re
data = ""
file = open("input.txt", "r")
for list in file:
    data += list
file.close()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, data)  

sum = 0
for string in matches:
    regex = r"\d+"
    matches_new = re.findall(regex, string)
    sum += int(matches_new[0]) * int(matches_new[1])

print(sum)
      
