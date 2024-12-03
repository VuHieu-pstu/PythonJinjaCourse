from jinja2 import Template

name = "Hieu"

data = '''Tai truong dai hoc bat khoa Perm
co mot NCS ten la {{a}}
anh ay rat thich lap trinh'''

t = Template(data)
msg = t.render(a=name)
print(msg)
print("------------------------")

#1. neu dat khoi {% raw %} {% endraw %} thi ngoac {{ }} nam giua khoi raw khong co tac dung
data = '''{% raw %}Tai truong dai hoc bat khoa Perm
co mot NCS ten la {{a}}
anh ay rat thich lap trinh{% endraw %}'''

t = Template(data)
msg = t.render(a=name)
print(msg)

#2. khoi lenh for
cities = [{'id':1, 'city': 'Ha Noi'},
          {'id':2, 'city': 'Sai Gon'},
          {'id':3, 'city': 'Hai Phong'},
          {'id':4, 'city': 'Da Nang'},
          {'id':5, 'city': 'Hung Yen'}]

link = '''<select name="cities">
{% for c in cities %}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>'''

t = Template(link)
msg = t.render(cities = cities)
print(msg)

link = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''

t = Template(link)
msg = t.render(cities = cities)
print(msg)
print("----------------------------")
#3. khoi if
link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 3 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "Hai Phong" -%}
    <option>{{c['city']}}</option>
{% else -%}
{{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

t = Template(link)
msg = t.render(cities = cities)
print(msg)