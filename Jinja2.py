# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('Window.html')
print(template.render(container=u'login'))