def move(disk):
    pass



def tower(n, a):
    moves = 0
    
    rods = {}
    biggest = n
    for i in range(4):
        rods[i+1] = []
    for row in a:
        rods[row] += [biggest]
        biggest -= 1
    # print(rods)
    positions = {}
    
    for row in rods.keys():
        for disk in rods[row]:
            positions[disk] = row
    print(rods)
    smallest = 1
    next_smallest = 2
    biggest_disk = n
    while len(rods[1]) < n:
        tops = {}
        empty = {}
        for row in rods.keys():
            if len(rods[row]) > 0:
                tops[rods[row][-1]] = row
            else:
                empty[row] = []
        if len(empty.keys()) > 0:
            last_empty = max(empty.keys())
        # print(len(empty.keys()))
        if len(rods[1]) > 0:
            if rods[1][-1] == biggest_disk:
                biggest_disk -= 1
            else:
                if rods[1][-1] == biggest_disk + 1 and biggest_disk in tops.keys():
                    rods[tops[biggest_disk]].remove(biggest_disk)
                    rods[1].append(biggest_disk)
                    biggest_disk -= 1
                    moves += 1
                    
                elif len(empty.keys()) > 0 and smallest in tops.keys():
                    rods[tops[smallest]].remove(smallest)
                    rods[last_empty].append(smallest)
                    smallest += 1
                    moves += 1
                    print(rods)
                else:
                    biggest_top = max(tops.keys())
                    rods[tops[smallest]].remove(smallest)
                    rods[tops[biggest_top]].append(smallest)
                    smallest +=1
        break            
    print(rods)    
    return moves
    
    
print(tower(4, [2, 1, 3, 2]))