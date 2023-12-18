oldlist = [10, 75, 43, 15, 25, -4, 27]#unsorted array

def bubble_sort(oldlist):#function with unsorted array
    last_item = len(oldlist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item - z):
            if oldlist[x] > oldlist[x+1]:
                oldlist[x], oldlist[x + 1] = oldlist[x+1], oldlist[x]

    return oldlist

print("Old list:", oldlist)
newlist = bubble_sort(oldlist).copy()
print("Mew list:", newlist)