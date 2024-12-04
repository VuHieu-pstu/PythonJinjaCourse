from jinja2 import Environment, FileSystemLoader

folder = FileSystemLoader('templates')
env = Environment(loader=folder)

t = env.get_template('page.html')
msg = t.render(domain='http://proproprogs.ru', title="Про Jinja")

print(msg)