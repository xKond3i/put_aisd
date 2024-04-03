def sort(arr: list[int], merges: int = 0) -> tuple[list[int], int]:
    if len(arr) <= 1:
        return arr, 0
 
    # dividing the array into two halves
    mid = len(arr) // 2
    L: list[int] = arr[:mid]
    R: list[int] = arr[mid:]

    # print(L, R) # <- check how the splitting goes

    # sorting the halves
    L, mL = sort(L)
    R, mR = sort(R)

    merges = mL + mR

    # print(L, R) # <- check how the sorting goes

    # merge the arrays
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # check if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    # print(arr) # <- check how the sorting goes (all the merges)

    return arr, merges + 1
