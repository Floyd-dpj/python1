# 使用构造方法进行赋值
class Student:
    name = None
    age = None
    tel = None
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        # print("Student类创建了一个类对象")
    def __str__(self):
        return f"Student类对象,name:{self.name},age:{self.age}"
stu1 = Student('floyd', 23, '15655222755')
# print(stu1.name + "\n")
# print(stu1.age)
# print(stu1.tel)
print(stu1)
