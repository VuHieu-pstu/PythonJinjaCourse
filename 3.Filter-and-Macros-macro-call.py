from jinja2 import Template

cars = [{'model': 'Honda', 'price': 10000},
        {'model': 'Toyota', 'price': 20000},
        {'model': 'Huyndai', 'price': 30000},
        {'model': 'Vinfast', 'price': 40000}]

tpl = "Tong gia cua cac oto {{ cs | sum(attribute = 'price') }}"
t = Template(tpl)
msg = t.render(cs=cars)
print(msg)

digs = [1, 2, 3, 4, 5]
tpl = "Tong cac so la {{ cs | sum }}"
t = Template(tpl)
msg = t.render(cs=digs)
print(msg)

tpl = "Mau o to dat nhat la {{ cs | max(attribute = 'price') }}"
t = Template(tpl)
msg = t.render(cs=cars)
print(msg)

tpl = "Mau o to re nhat la {{ (cs | min(attribute = 'price')).model }}"
t = Template(tpl)
msg = t.render(cs=cars)
print(msg)

tpl = "Chon loai bat ky {{ cs | random }}"
t = Template(tpl)
msg = t.render(cs=cars)
print(msg)

persons = [{"name": "Hieu", "old": 37, "weight": 70},
           {"name": "Hoi", "old": 38, "weight": 50},
           {"name": "Phong", "old": 11, "weight": 30},
           {"name": "Ngoc", "old": 3, "weight": 14}]

tpl = '''
{% for p in users -%}
    {% filter upper %}{{p.name}}{% endfilter %}
{% endfor %}'''

t = Template(tpl)
msg = t.render(users=persons)
print(msg)

tpl = '''
{% for p in users -%}
    {% filter lower %}{{p.name}}{% endfilter %}
{% endfor %}'''

t = Template(tpl)
msg = t.render(users=persons)
print(msg)

html = '''
{% macro input(name, value="", type="text", size=20) -%}
    <input type = "{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}</p>
<p>{{ input('email') }}</p>
<p>{{ input('password') }}</p>
'''
t = Template(html)
msg = t.render()
print(msg)