class_list = ["python", "c", "c++", "c#", "java"]
for class_ in class_list:
    print(class_)

sum = 0
for i in range(1, 100 + 1):
    sum = sum + i

info_dict = {"name": "song", "age": 20, "job": "developer"}
for info in info_dict:
    print(info)  # only key

for info_key, info_value in info_dict.items():
    print(info_key, info_value)  # key, value

some_string = "hello world"
for i, v in enumerate(some_string):
    print("{}번째 요소{} ".format(i, v))

for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))

while class_list:
    print(class_list)
    class_list.pop()

cnt = 1
while cnt <= 10:
    print("while {} ".format(cnt))
    cnt += 1

cnt = 1
while True:
    if cnt == 5:
        print("break!!!")
        break
    else:
        print("While {}".format(cnt))
        cnt += 1

list1 = []

for i in range(1, 3 + 1):
    list1.append(i)

list2 = ["one", "two", "three"]

for n, v in zip(list2, list1):
    print(n, v)