class Student:
    name = None
    def sayhi1(self,mag):
        print(f"大家好"+mag)
    def sayhi(self):
        print(f"大家好呀，我是{self.name},欢迎大家多多关照")
student = Student()
student.name = 'floyd'
student.sayhi1(mag = 'mah')
student.sayhi()