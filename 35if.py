x = 15

if x >= 10:
    print(x)

score = 85

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
else:
    print("학점 : F")

if score >= 70:
    print("성적이 70점 이상입니디.")
    if score >= 90:
        print("우수한 성적입니다.")
else:
    print("성적이 70점 미만입니다.")
    print("조금 더 분발하세요")

print("프로그램을 종료합니다.")

score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드,
else:
    print('성적이 80점 미만입니다.')

print ('프로그램을 종료합니다.')

result = "Success" if score >= 80 else "Fail"
print(result)

a = [1,2,3,4,5,5,5]
remove_set = [3,5]

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}
result =[]

result = [i for i in a if i not in remove_set]

print(result)
