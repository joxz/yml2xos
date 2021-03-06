import yaml
import jinja2
import os


with open('sw.yml', 'r') as f:
    i = yaml.load(f)


jenv = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.getcwd()),
    trim_blocks=True, lstrip_blocks=True
)

template = jenv.get_template('sw.j2')


print template.render(item = i)

#with open(i['name'] + '.xsf', 'w') as out:
#    out.write(template.render(item = i))
