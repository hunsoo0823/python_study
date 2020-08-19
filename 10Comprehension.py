old_list = [1,2,3,4,5]
double_list = [i * 2 for i in old_list]
third_list = [i * 2 for i in old_list if i % 2 == 0]

print(double_list)
print(third_list)

gugu_list = ["{} * {} = {}".format(i,j,i*j) for i in range(1,9+1) for j in range(1,9+1)]
print(gugu_list)

list1 = [i for i in range(1,4+1)]
list2 = ["one","two","three","four"]

list_to_dict = {k : v for k, v in zip(list1, list2) }
print(list_to_dict)