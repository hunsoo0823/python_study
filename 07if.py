import random

answer = random.randint(1,100)
your_anwser = eval(input("숫자를 입력해주세요."))

if answer == your_anwser:
    print("정답")
else:
    print("오답")