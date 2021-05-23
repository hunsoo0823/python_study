def binarySearch(start, end, target, array):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] > target:
        return binarySearch(start, mid-1, target, array)
    elif array[mid] < target:
        return binarySearch(mid+1, end, target, array)
    else:
        return mid

n, target = map(int, input().split())

array = list(map(int, input().split()))
result = binarySearch(0, n-1, target, array)

if result != None:
    print(result+1)
else:
    print("원소가 존재하지 않습니다.")