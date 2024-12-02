lists = []
file = open("input.txt", "r")
for line in file:
    line_split = line.split()
    lists.append([int(item) for item in line_split])
file.close()

def differ(list, x,y):
    return (0 < abs(list[x]-list[y]) < 4)

def is_safe(list):
    i = 1
    n = len(list)
    decreasing  = list[0] > list[1]
    if decreasing and differ(list, 0,1) :
        while list[i] > list[i+1] and differ(list, i,i+1):
            i += 1
            if (i+1) == n:
                return 1
    elif differ(list, 0,1):
        while list[i] < list[i+1] and differ(list, i,i+1):
            i += 1
            if (i+1) == n:
                return 1
    return 0

def count_safes(data):
    for idx in range(len(data)):  
        data_removed = data[:idx] + data[idx + 1:]
        if is_safe(data_removed):
            return 1
    return 0
        
safe = 0  
for list in lists:
    safe += count_safes(list)

print(safe)