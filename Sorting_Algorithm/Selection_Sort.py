# default implementation of selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        if min_ind != i:
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr


# selection sort for strings
def selection_sort_string(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        if min_ind != i:
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr


# implementation of stable selection sort
def stable_selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        key = arr[min_ind]
        while min_ind > i:
            arr[min_ind] = arr[min_ind-1]
            min_ind -= 1
        arr[i] = key
    return arr


if __name__ == "__main__":
    a = [36, 1, 14, 78, 13]
    b = ["Ice", "Happy", "Shreya", "Cat", "Play"]
    c = [1, 4, 11, 1, 6, 4]
    print(selection_sort(a))
    print(selection_sort_string(b))
    print(stable_selection_sort(c))
