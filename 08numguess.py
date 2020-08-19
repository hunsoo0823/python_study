"""
숫자 맞추기 게임
1. 컴퓨터가 난수를 실행한다. (범위는 1~100)
2. 사용자 부터 숫자를 입력받는다.
3. 입력받은 숫자가 난수와 같은지 비교한다.
4. 문제가 맞출 수 있는 기회만을 반복한다.(기회5편)
5-1 틀렸을 경우 힌트를 제공한다.
5-2 사용자가 입력한 숫자가 정답보다 큰지,작은지를 알려준다.
6. 기회를 다썻다면 종료
7. 정답을 맞췄을떄도 종
"""

import random as rd

def numguess(try_cnt, answer):
    while True:
        if try_cnt == 0:
            print("기회를 모두 소진하였습니다")
            print("정답 : 정답은 {} 였습니다. ".format(answer))
            break
        else:
            your_input = eval(input("장답을 입력해주세요 : "))

        if answer == your_input:
            print("정답 : 정답은 {} 였습니다.".format(answer))
            break
        else:
            if answer > your_input:
                print("정답은 {}보다 큽니다.".format(your_input))
                try_cnt -= 1
            else:
                print("정답은 {} 보다 작습니다.".format(your_input))
                try_cnt -= 1

answer = rd.randint(1,100)
try_cnt = 5

numguess(try_cnt, answer)