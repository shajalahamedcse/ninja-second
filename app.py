import json
from model.person import Person
from model.employee import Employee

    
p1 = Person("shajal",27)
p2 = Person("Simon",27)
p3 = Person("Iftekhar",27)
plist = [p1,p2,p3]

with open("person_list.json","w",encoding='utf-8') as f:
    for p in plist:
        f.write(p.to_json()+"\n")
        
e1 = Employee("Shajal",27,10,'cse')
print(e1.name)
    