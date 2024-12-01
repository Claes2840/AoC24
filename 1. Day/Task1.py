list1 = []
list2 = []
file = open("data.txt", "r")

for line in file:
    line_split = line.split()
    list1.append(int(line_split[0]))
    list2.append(int(line_split[1]))

list1 = sorted(list1)
list2 = sorted(list2)

sum = 0
for idx,elm in enumerate(list1):
    sum += abs(elm - list2[idx])
    
print(sum)