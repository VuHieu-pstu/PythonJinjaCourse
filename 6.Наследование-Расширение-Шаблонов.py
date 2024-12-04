from jinja2 import Environment, FileSystemLoader

subs = ["Toan", "Ly", "Hoa", "Tin"]

folder = FileSystemLoader('templates')
env = Environment(loader=folder)

t = env.get_template('about.html')
msg = t.render(list_table=subs)
print(msg)