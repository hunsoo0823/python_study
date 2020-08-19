new_text="winner winner chicken dinner"
print("Left:",new_text[0],new_text[1],new_text[2],new_text[3],new_text[4],new_text[5])
print(new_text[0:6]) # 0<=index<n

cs_all_in_one="python,c,c++,programming"
cs_all_in_one_list = cs_all_in_one.split(",")
print(cs_all_in_one_list)

cs_all_in_one_str = ",".join(cs_all_in_one_list)
print(cs_all_in_one_str)

python = "파이썬"
before = "cs all in one %s " % python
after = "cs 올인원{}". format(python)
print(before)
print(after)