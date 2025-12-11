def rotate_arr_left(arr, n):
    length = len(arr)

    n = n % length

    if n == 0:
        return arr.copy()
    rotated = []
    rotated.extend(arr[n:])
    rotated.extend(arr[:n])

    return rotated

arr1 = [3,5,3,6,2,8,45,9]
n1 = 68
print(rotate_arr_left(arr1, n1))