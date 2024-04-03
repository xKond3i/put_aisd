def sort(arr: list[int]) -> list[int]:
    stack: list[int] = [] # create stack of array's bounds, that need sorting
    # bounds obtaianing the whole array
    stack.append(0) # lower bound
    stack.append(len(arr) - 1) # higher bound

    # while there are bounds to be sorted
    while stack:
        higher_bound: int = stack.pop()
        lower_bound:  int = stack.pop()
        pivot_idx: int = partition(arr, lower_bound, higher_bound) # get the new pivot (element that was greater than the previous pivot) index

        # defining new bounds based on the new pivot
        if pivot_idx - 1 > lower_bound: # == L (left subarray)
            stack.append(lower_bound)
            stack.append(pivot_idx - 1)
        if pivot_idx + 1 < higher_bound: # == R (right subarray)
            stack.append(pivot_idx + 1)
            stack.append(higher_bound)

    return arr

def partition(arr: list[int], lower_bound: int, higher_bound: int) -> int:
    # z pivotem, którym jest skrajnie prawy element ciągu (ostatni element listy)
    pivot = arr[higher_bound]
    i = lower_bound - 1

    for j in range(lower_bound, higher_bound):
        if arr[j] > pivot:
            continue
        i += 1
        arr[i], arr[j] = arr[j], arr[i] # swapping elements

    arr[i + 1], arr[higher_bound] = arr[higher_bound], arr[i + 1] # swapping the next biggest element with pivot (pivot has to land between the subarrays)

    return (i + 1) # new pivot index
