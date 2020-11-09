from .person import Person

class Employee(Person):
    def __init__(self, name, age, salary, dep):
        super().__init__(name, age)
        self.salary = salary
        self.dep = dep
        

        