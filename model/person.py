import json

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'Person ({},{})'.format(self.name,
                                         self.age)
    def to_dictionary(self):
        return {
            "name": self.name,
            "age": self.age
        }
    def to_json(self):
        p = {
            "name": self.name,
            "age": self.age
        }
        return json.dumps(p)