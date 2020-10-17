import sys

# 데이터 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

# 문자열 입력받기

data = sys.stdin.readlines().rstrip()
print(data)
