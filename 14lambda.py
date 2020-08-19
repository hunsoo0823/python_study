some_list = [1,2,3,4,5]
result = list(map(lambda x:x*2,some_list))
print(result)

some2_list = [1,"1","one",4.567,{1:"one"}]
result2 = list(filter(lambda x: isinstance(x,str) ,some2_list))
print(result2)