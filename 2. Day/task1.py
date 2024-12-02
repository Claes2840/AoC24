lists = []
file = open("input.txt", "r")
for line in file:
    line_split = line.split()
    lists.append([int(item) for item in line_split])
file.close()

safe = 0  
def differ(x,y):
    return (0 < abs(list[x]-list[y]) < 4)

def is_safe(list):
    i = 1
    n = len(list)
    decreasing  = list[0] > list[1]
    if decreasing and differ(0,1) :
        while list[i] > list[i+1] and differ(i,i+1):
            i += 1
            if (i+1) == n:
                return 1
    elif differ(0,1):
        while list[i] < list[i+1] and differ(i,i+1):
            i += 1
            if (i+1) == n:
                return 1
    return 0

for list in lists:
    safe += is_safe(list)
    
print(safe)