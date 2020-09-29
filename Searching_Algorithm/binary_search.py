def binary_search_recursive(arr, si, ei, ele):
    if si <= ei:
        mid = (si + ei) // 2
        if arr[mid] == ele:
            print("Position of element is", mid+1)
        elif arr[mid] < ele:
            binary_search_recursive(arr, mid+1, ei, ele)
        else:
            binary_search_recursive(arr, si, mid-1, ele)
    else:
        print("Element not found")


def binary_search_iterative(arr, si, ei, ele):
    while si <= ei:
        mid = (si + ei) // 2
        if arr[mid] == ele:
            print("Position of element is", mid + 1)
            break
        elif arr[mid] < ele:
            si = mid+1
        else:
            ei = mid-1
    else:
        print("Element not found")


array = [2, 3, 4, 10, 40]
element = int(input("Enter the element:-"))
binary_search_recursive(array, 0, len(array)-1, element)
binary_search_iterative(array, 0, len(array)-1, element)
