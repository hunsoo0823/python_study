a = 1000 # 양의 정수
print(a)

a = -7 # 음의 정수
print(a)

a = 0 # 0
print(a)

a = 157.93 # 양의 실수
print(a)

a = -1873.2 # 음의 실수
print(a)

a = 5. # 소수부가 0일 때 0의 생략
print(a)

a = -.7 # 정수부가 0일 때 0을 생략
print(a)

a = 1e9 #10억
print(a)

a =75.25e1 # 752.5
print(a)

a= 3582e-3 # 3.582
print(a)

a = 0.3+0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

a = 0.3 + 0.6
print(round(a,4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

a = 7
b = 3

# 나누기
print(a/b)

# 나머지
print(a%b)

# 몫
print(a//b)

a = 5
b = 3
print(a ** b)

a = [1,2,3,4,5,6,7,8,9]
print(a)

# 인덱스 4, 즉 다섯 번째 원소에 접근
print(a[4])

#빈 리스트 선언 방법 1)
a = list()
print(a)

# 2)
a =[]
print(a)

a = [1,2,3,4,5,6,7,8,9]
print(a[-1]) # 뒤에서 첫 번째 원소 출력

print(a[-3]) # 뒤에서 세 번째 원소 출력

a[3] = 7 # 네 번째 원소 값 변경
print(a)

a = [1,2,3,4,5,6,7,8,9]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# 0 부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1 부터 9까지의 수의 제곱 값을 포함하는 리스
array = [i * i for i in range(1,10)]
print(array)

# N x M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# N X M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

a = [1,4,3]
print("기본 리스트:", a)

# 리스트에 원소 집합
a.append(2)
print("삽입 : ",a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ",a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ",a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ",a)

# 특정 인텍스 데이터 추가
a.insert(2,3)
print("인덱스 2에 3추가: ",a)

# 특정 값 데이터 개수 추가
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("갑이 1인 데이터 삭제:", a)

a = [1,2,3,4,5,5,5]
remove_set = [3,5]

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

data = 'Hello world'
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"

print(a+" "+b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2:4])

a = (1,2,3,4)
print(a)

# a[2] = 7 error

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 집합 자료형 초기화 방법 1
data = set([1,1,2,3,4,5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1,1,2,3,4,4,5}
print(data)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합

data = set([1,2,3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 워소 여러개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

