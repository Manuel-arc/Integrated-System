import xmltodict
import json

class Products:

    def __init__(self, dic):
        self.student_grade = dic

    def get_basket_price(self, basket):
        a = 0
        for i in range(len(basket)):
            if basket[i] in self.student_grade:
                a += self.student_grade[basket[i]]
            else:
                a = basket[i]+" não existe"
                break

        return a


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

stu = Products(dic)

a = stu.get_basket_price(["Joao", "Mateus"])

print(a)
