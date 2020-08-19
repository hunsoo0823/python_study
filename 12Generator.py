import sys
import time

def lazy_evaluation(n):
    print("1 sec sleep")
    time.sleep(1)
    return n

def generator():
    yield "hello"
    yield "python"
    yield 11

gen = generator()
print(next(gen)) # hello
print(next(gen)) # python
print(next(gen)) # 11
#print(next(gen)) # StopIteration

print(sys.getsizeof([i for i in range(1,10000 + 1)]))
print(sys.getsizeof((j for j in range(1,10000 + 1))))

n_list = [lazy_evaluation(n) for n in range(1,5+1)]
for i in n_list:
    print(i)
n_generator =(lazy_evaluation(n) for n in range(1,5+1))
for j in n_generator:
    print(j)