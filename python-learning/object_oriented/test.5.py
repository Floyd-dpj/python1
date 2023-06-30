class Student:
    name = None
    age = None
    add = None
    def __init__(self,name ,age, add):
        self.name = name
        self.age = age
        self.add = add
        print(f"学生姓名:{self.name},年龄：{self.age},地址:{self.add}")
count = [1,2,3,4,5,6,7,8,9,10]
for i in count:
    print(f"当前录入第{i}位学生信息，总共需要录入10位学生信息")
    stu = Student(input('请输入姓名:'), input('请输入性别:'), input('请输入地址:'))
    print(f"学生{i}信息录入完成，信息为：【学生姓名:{stu.name},年龄：{stu.age},地址:{stu.add}】")

