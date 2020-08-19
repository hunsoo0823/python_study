#list
var1 = [1,"list",2,"campus",3,"ollinone"]
var2 = [] # empty list
var3 = () # empty tuple
var5 = [5,4,3,2,1]

print(var1[0],var1[3])
print(var1[0:3]) # slicing 0<=index<3

var1.append("slicing")
var4 = var1 + var2
var1.extend(var2)
var2.insert(1,"car")
var2.insert(3,"bus")
var1.remove("campus")
del var1[0] # delet
print(var1)
print(var1.count(1))
print(len(var1))
print(var1.index(3)) # find index
var5.sort() # sort