def bubble_sort(arr):
    new_arr = arr.copy()
    n = len(new_arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            try:
                if new_arr[j] > new_arr[j + 1]:
                    new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
            except TypeError:
                print('ERROR! Values must be numbers')
                raise ValueError
    return new_arr
