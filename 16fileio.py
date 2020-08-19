f = open("some.txt","w")
for i in range(1,9+1):
    data = "5 * {} = {}\n".format(i,5*i)
    f.write(data)

f = open("some.txt","r")
print(f.read())
while True:
    data = f.readline()
    if not data:
        break
    print(data, end='')
data = f.readlines()
f.close()
for line in data:
    print(line,end='')