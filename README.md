# Algorithm_python
Implementation of all algorithms in python.
# Sorting_Algorithm

## Selection Sort

[Selection Sort](Selection_Sort.py)

| Case | Complexity |
| ----------- | ----------- |
| `Worst Case` | **O(n^n)** |
| `Average Case` | **O(n^n)** |
| `Best Case`  |  **O(n^n)**|
| `Auxiliary Space` | **O(1)**|


## Bubble Sort

[Bubble Sort](Bubble_Sort.py)

| Case | Complexity |
| ----------- | ----------- |
| `Worst Case` | **O(n^n)** |
| `Average Case` | **O(n^n)** |
| `Best Case`  |  **O(n)**|
| `Auxiliary Space` | **O(1)**| 

   

# Searching_Algorithm
Algorithms to check for an element or retrieve an element from any data structure where it is stored.
## Linear Search

[Linear Search](linear_search.py)

* It is a sequential search algorithm i.e. the list or array is traversed sequentially and every element is checked.
* It is rarely used practically.

| Case | Complexity |
| ----------- | ----------- |
| `Worst Case` | **O(n)** |
| `Average Case` | **O(n)** |
| `Best Case`  |  **O(1)**|
| `Auxiliary Space` | **O(1)**|

## Binary Search

[Binary Search](binary_search.py)

* It is an interval search algorithm.
* This algorithms is specifically designed for searching in sorted data-structures. 
* This type of searching algorithm is much more efficient than Linear Search.
* It employs recursive approach which requires more stack space.
* The interaction of binary search with memory hierarchy i.e. caching is poor.

| Case | Complexity |
| ----------- | ----------- |
| `Worst Case` | **O(log n)** |
| `Average Case` | **O(log n)** |
| `Best Case`  |  **O(1)**|
| `Auxiliary Space (iterative) `| **O(1)**|
| ` Auxiliary Space (recursive)`|**O(log n)**|

## Jump Search

[Jump Search](https://github.com/dhandashreya/Algorithm_python/blob/master/Searching_Algorithm/jump.py)

* It is also called block search algorithm.
* This algorithm works only for sorted arrays or lists.
* Optimal size of the block to be skipped is √n.
* Time complexity of this algorithm lies between linear search and binary search.
* This algorithm needs to jump backwards only once but binary search can jump backwards upto log n times.

| Case | Complexity |
| ----------- | ----------- |
| `Worst Case` | **O(√n)** |
| `Average Case` | **O(√n)** |
| `Best Case`  |  **O(1)**|
| `Auxiliary Space` | **O(1)**|
