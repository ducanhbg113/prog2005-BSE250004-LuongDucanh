def selection_sort(a):
    n = len(a)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


arr = [5, 2, 9, 1, 3]

print(selection_sort(arr))