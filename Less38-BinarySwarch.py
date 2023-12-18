def binarysearch(mylist, iskat, start, stop):#function binarysearch search in the mylist a digit=iskat starting from start untill the end=stop
    if start > stop:#if we will start to search from an index which is greater than the last one, than return False
        return False
    else:
        mid = (start + stop) // 2#delit massiv popolam, // - delenie vozvraschaet vsegda celoe chislo
        if iskat == mylist[mid]:#if number = to middle than return mid
            return mid
        elif iskat < mylist[mid]:#if lower than search to a first part of the array
            return binarysearch(mylist, iskat, start, mid - 1)
        else:
            return binarysearch(mylist, iskat, mid + 1, stop)#if greater than search to a second part of the array

mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]#Array where we are searching
iskat = 81#a number which is wanted in the array
start = 0#the start of index of array Ex: Index0=10 Index1=12 Index2=13 Index3=15 etc
stop = len(mylist)#quandtity of indexes equal to a length of array it means that the last index is equal to a length of the array

x = binarysearch(mylist, iskat, start, stop)#x will be equal to a result of the function binarysearch

if x == False:
    print("ITEM ", iskat, "NOT FOUND")
else:
    print("ITEM", iskat, "FOUND at Index", x)