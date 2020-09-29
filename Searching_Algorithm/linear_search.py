# implementation of traditional linear search
def linear_search(arr, n, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1


# implementation of sentinel linear search
def sentinel_linear_search(arr, n, ele):
    last = arr[n-1]
    arr[n-1] = ele
    i = 0
    while arr[i] != ele:
        i += 1
    arr[n-1] = last
    if i < n-1 or arr[n-1] == ele:
        print("Position of element by sentinel linear search is", i+1)
    else:
        print("Element not found")


# implementation of linear search on a an ordered list
def ordered_linear_search(arr, n, ele):
    i = 0
    while i < n:
        if arr[i] == ele:
            print("Position of element by ordered linear search is", i + 1)
            break
        elif arr[i] > ele:
            print("Element not found")
            break
        i += 1


array = [2, 3, 4, 10, 40]
element = int(input("Enter the element to be searched:-"))
length = len(array)
result = linear_search(array, length, element)
if result == -1:
    print("Element not found")
else:
    print("Position of element by linear search is", result+1)

sentinel_linear_search(array, length, element)
ordered_linear_search(array, length, element)
