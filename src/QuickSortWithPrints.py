'''
QUICKSORT Algorithm
Directly following the pseudocode from CLRS
Allows for change of pivot choice (left, right or random within subArray
'''

from random import randint


def quickSort(p, r):
    itercount[0] += 1
    print(f"Quicksort iteration: {itercount[0]}, P = {p}, R = {r}")
    if p < r:
        q = partition(p, r)
        print(f"P = {p}, Q-1 = {q - 1}")
        quickSort(p, q - 1)
        print(f"Q+1 = {q}, R = {r}")
        quickSort(q + 1, r)


def partition(p, r):
    itercount[1] += 1
    # Select pivot by commenting/uncommenting the pivot selections below
    # pivot = r  # basic version of Quicksort - always chooses rightmost element as pivot
    # pivot = p  # always chooses leftmost element as pivot
    pivot = randint(p, r)  # randomised pivot. Picks pivot within the subarray then swaps so pivot becomes last element

    arr[pivot], arr[r] = arr[r], arr[pivot]  # move pivot to last place (no effect if pivot = r)

    v = arr[r]  # pivot value

    print(f"Partition, iteration {itercount[1]}, from {p} to {r}. Pivot value is {v}")
    print(f"  Sub-array before partition: {arr[p:r + 1]}")

    i = p - 1
    for j in range(p, r):
        if arr[j] <= v:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    print(f"  Sub-array after partition: {arr[p:r + 1]}")
    return i + 1


def main():
    global arr  # Array defined as global so that it is available to all methods without being passed
    global itercount  # Count iterations
    # arr = [54, 23, 13, 546, 234, 412, 12, 32, 543, 41, 1342, 421, 1232, 2, 1]
    arr = [5, 8, 1, 3, 7, 9, 2]
    itercount = [0, 0]  # itercount[0] to count calls to quickSort, [1] to count calls to partition
    print(f"Array before sorting: {arr}")
    quickSort(0, len(arr) - 1)
    print(f"Array after sorting: {arr}")
    print(f"Number of method calls. Quicksort: {itercount[0]}, Partition {itercount[1]}")


if __name__ == '__main__':
    main()
