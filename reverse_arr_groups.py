def reverse_in_groups(arr, n):
    length = len(arr)
    for i in range(0, length, n):
        left = i
        right = min(i+n-1,length-1)
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

arr1 = [1,2,4,5,6,3,6,3,6,4,6,8]
n1 = 3
print(reverse_in_groups(arr1, n1))