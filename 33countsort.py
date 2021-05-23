
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
print()

array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

array = [7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

array = [('바나나', 2), ('사과',5), ('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)