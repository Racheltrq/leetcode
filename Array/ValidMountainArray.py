def validMountainArray(self, arr):
    print("\nstart\n")
    if len(arr) < 3:
        return False
    up = down = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]:
            if up == 0:
                up = 1
            if down == 1:
                return False
        if arr[i] > arr[i+1]:
            if up == 0:
                return False
            down = 1
        if arr[i] == arr[i+1]:
            return False
    if up == down == 1:
        return True
    else:
        return False