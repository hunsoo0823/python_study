import requests
from bs4 import BeautifulSoup

URL = "https://www.fastcampus.co.kr/online_category"

response = requests.get(url=URL)
# print(response.text) # response = 200 is successfully response
soup = BeautifulSoup(response.text,"html.parser")
get_all_course = soup.find_all("div",{"class":"vn-product-list__info"})

def parsing_course(elements):
    title =elements.find("strong").text
    money = elements.find("i").text
    open = elements.find("span").text
    sup = elements.find("p").text
    print("강의 제목 : {}".format(title))
    print("수강료 : {}".format(money))
    print("오픈 : {}".format(open))
    print("설명 : {}".format(sup))
    print("-"*100)

for i in get_all_course:
    parsing_course(i)
    #print(i)

print("패스트 캠퍼스 프로그래밍의 강의 갯수는 {}개 입니다.".format(len(get_all_course)))