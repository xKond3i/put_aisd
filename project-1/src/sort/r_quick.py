def sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    # z pivotem, którym jest skrajnie prawy element ciągu (ostatni element listy)
    pivot_idx = len(arr) - 1
    pivot = arr[pivot_idx]

    less_than_pivot = [x for x in arr[:pivot_idx] if x <= pivot]
    more_than_pivot = [x for x in arr[:pivot_idx] if x >  pivot]

    # print(less_than_pivot, pivot, more_than_pivot) # <- check how the sorting goes

    return sort(less_than_pivot) + [pivot] + sort(more_than_pivot) # combining lists
