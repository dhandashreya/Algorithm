# implementation of bubble sort
def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# implementation of optimized bubble sort
def optimized_bubble_sort(arr, n):
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# recursive implementation of bubble sort
def recursive_bubble_sort(arr, n):
    if n == 1:  # base case
        return arr
    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        recursive_bubble_sort(arr, n-1)
    return arr


if __name__ == "__main__":
    a = [54, 11, 2, 35, 98, 71, 113]
    length = len(a)
    print(bubble_sort(a, length))
    print(optimized_bubble_sort(a, length))
    print(recursive_bubble_sort(a, length))
