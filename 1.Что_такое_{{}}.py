from jinja2 import Template

name = "Hieu"
age = 28

t1 = Template("Hello {{a}}")
msg = t1.render(a=name)

msg2 = f"Hello {name}"

print(msg,msg2, sep="\n")
#----------------------------------

t2 = Template("Toi ten la {{n}} va {{a}} tuoi")
msg3 = t2.render(n=name, a=age)
print(msg3)

#----------------------------------

t4 = Template("Toi ten la {{n.upper()}} va {{a*2}} tuoi")
msg4 = t4.render(n=name, a=age)
print(msg4)

#----------------------------------
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

p = Person("Hieu", 33)

t4 = Template("Toi ten la {{n.upper()}} va {{a*2}} tuoi")
msg4 = t4.render(n=p.name, a=p.age)
print(msg4)

t4 = Template("Toi ten la {{n.upper()}} va {{a*2}} tuoi")
msg4 = t4.render(n=p.getName(), a=p.getAge())
print(msg4)

#-----------------------------------------------------

per = {'name':'Hieu', 'age': 37}

t = Template("Toi ten la {{p.name}}. Hien nay toi {{p.age}} tuoi")
msg = t.render(p=per)
print(msg)

t = Template("Toi ten la {{p['name'].upper()}}. Hien nay toi {{p['age']}} tuoi")
msg = t.render(p=per)
print(msg)