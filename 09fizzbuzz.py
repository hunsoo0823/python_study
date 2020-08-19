"""
1. 3의 배수 Fizz
2. 5의 배수 Buzz
3. 15의 배수 Fizz,Buzz
"""

def fizzBuzz(i):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)

for i in range(1,100+1):
    fizzBuzz(i)