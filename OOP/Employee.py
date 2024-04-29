class Parent:
    def __init__(self):
        print("parent initialization done ..")

    def sayhi(self):
        print("Hi......")


class Employee(Parent):
    def __init__(self, name, age, education):
        self.name = name
        self.age = age
        self.education = education

    def get_work(self):
        if self.education == "BE":
            print(self.name + " will do engineer work")
        elif self.education == "BCom":
            print(self.name + " will do finance work")

    def salary(self):
        if self.education == "BE":
            print(self.name + " have big salary")
        elif self.education == "BCom":
            print(self.name + " have low salary")


emp = Employee("John", 25, "BE")
emp.get_work()
emp.salary()
emp.sayhi()

emp1 = Employee("Eva", 26, "BCom")
emp1.get_work()
emp1.salary()
emp.sayhi()