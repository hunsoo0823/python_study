class Parents: #부모 클래
    father ="song"

    def father_name(self):
        print(self.father)

class Myson(Parents): # 자식클래스
    def __init__(self,name,age,kind,distinct,speak):
        self.name = name
        self.age = age
        self.kind = kind
        self.distinct = distinct
        self.speak = speak

    def bark(self):
        print(self.speak)

    def father_name(self): # 메서드 오버라이
        print("저의 아버지는 song입니다.")

bokgil = Myson("복길", "Unknown","Unknown", "사람을 좋아함", "멍멍")
chapssal = Myson("찹쌀", "20day", "mix", "cute", "낑낑")
cloud = Myson("구름","6month","mix","very cute","야옹")
print(cloud.name)
print(cloud.age)
print(cloud.kind)
print(cloud.distinct)

bokgil.father_name()
chapssal.father_name()
cloud.father_name()

bokgil.bark()
chapssal.bark()
cloud.bark()

print(dir(list)) #list가 가지고 있는 기능들을 알 수 있다.
print(dir(Myson)) #Myson객체가 가지고 있는 기능