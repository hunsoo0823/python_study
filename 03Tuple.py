t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3,4
t5 = 1,

#tuple unpacking
c1 = "red"
c2 = "blue"
colors = c1,c2
print(type(colors))
print(c1,c2)
c1,c2 = c2,c1   
print(c1,c2)