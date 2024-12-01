list1 = []
list2 = []
file = open("data.txt", "r")
for line in file:
    line_split = line.split()
    list1.append(int(line_split[0]))
    list2.append(int(line_split[1]))
    
Dict = {}
for idx,elm in enumerate(list1):
    Dict[idx] = elm*list2.count(elm)

print(sum(Dict.values()))