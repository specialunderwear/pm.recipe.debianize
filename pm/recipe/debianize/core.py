import logging, os, zc.buildout
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('pm.recipe.debianize', 'templates'))

class Debianize:

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        # options['path'] = os.path.join(
        #                       buildout['buildout']['directory'],
        #                       options['path'],
        #                       )
        # if not os.path.isdir(os.path.dirname(options['path'])):
        #     logging.getLogger(self.name).error(
        #         'Cannot create %s. %s is not a directory.',
        #         options['path'], os.path.dirname(options['path']))
        #     raise zc.buildout.UserError('Invalid Path')


    def install(self):
        template = env.get_template('debianize.sh')
        output = template.render(**options)
        # path = self.options['path']
        # logging.getLogger(self.name).info(
        #     'Creating directory %s', os.path.basename(path))
        # os.mkdir(path)
        # return path

    def update(self):
        pass