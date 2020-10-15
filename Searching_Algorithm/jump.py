import math
flag = 0


def jump_search(arr, ele):
    global flag
    interval = int(math.sqrt(len(arr)))
    for i in range(0, len(arr), interval):
        if arr[i] == ele:
            return i+1
        if arr[i] > ele:
            block = i
            flag = 1
            break
    if flag == 1:
        for j in arr[i:]:
            if arr[i] == ele:
                return i+1
            else:
                i -= 1
    else:
        return "not found"


my_list = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
val1 = 56
val2 = 13
print("Position of value {} is".format(val1), jump_search(my_list, val1))
print("Position of value {} is".format(val2), jump_search(my_list, val2))
