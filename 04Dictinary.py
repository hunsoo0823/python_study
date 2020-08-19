empty_dict={}
empty_dict = dict()
hong3_info = {
    "name":"song hyeon soo",
    "age" : 20,
    "job":"developer"
    }

print(hong3_info["name"]) # song hyeon soo

sample_list=[["nmae","song hyeon soo"],["age",20],[
"job","developer"]]
print(dict(sample_list))
sample_list =["ab","cd","ef"]
sample_set = ("ab","cd","ef")
print(dict(sample_list))
print(dict(sample_set))

#add dictionary
sample2_dict = {"name":"song hyeon soo"}
sample2_dict["nickname"] = "hong3"
sample2_dict["name"]="hong3"

sample3_dict = {"name":"kim min sick"}
sample4_dict = {}
sample4_dict.update(sample2_dict)
sample4_dict.update(sample3_dict) # 덮어쓰기
print(sample4_dict)

print(hong3_info.keys()) # print key
print(hong3_info.values()) # print value
print(hong3_info.items())
del hong3_info["age"]
hong3_info.clear()