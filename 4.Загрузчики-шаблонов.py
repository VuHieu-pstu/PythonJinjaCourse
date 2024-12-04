from jinja2 import Environment, FileSystemLoader

persons = [{"name": "Hieu", "old": 37, "weight": 70},
           {"name": "Hoi", "old": 38, "weight": 50},
           {"name": "Phong", "old": 11, "weight": 30},
           {"name": "Ngoc", "old": 3, "weight": 14}]

folder = FileSystemLoader('templates')
env = Environment(loader=folder)

t = env.get_template('main.html')
msg = t.render(users=persons)

print(msg)