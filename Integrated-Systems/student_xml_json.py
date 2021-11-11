import xmltodict
import json

class Student:

    def __init__(self, dic):
        self.student_grade = dic

    def check_student(self, name):
        if name in self.student_grade:
            return self.student_grade[name]

    def xml_parse(self):
        return xmltodict.unparse(self.student_grade)

    def json_parse(self):
        return json.dumps(self.student_grade)

dic = {
    'alunos':{
        "Joao": 23,
        "Mateus": 34,
        "Francelino": 21
    }
}

stu = Student(dic)

a = stu.student_grade

print(a)

b = stu.json_parse()

print(b)

c = stu.xml_parse()

print(c)
