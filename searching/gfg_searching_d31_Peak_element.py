def peakElement(arr):
    n = len(arr)

    for i in range(n):
        left = True
        right = True

        if i > 0 and arr[i] <= arr[i - 1]:
            left = False

        if i < n - 1 and arr[i] <= arr[i + 1]:
            right = False

        if left and right:
            return i


 
if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 3]
    print(peakElement(arr))
