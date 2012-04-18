import stat
from os import chmod
from os.path import join, isfile, sep

from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('pm.recipe.debianize', 'script'))


class Debianize:

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        self.bin = buildout['buildout']['bin-directory']
        self.fpm_path = (self.bin + sep) if isfile(join(self.bin, 'fpm')) else ""
        self.pip_path = (self.bin + sep) if isfile(join(self.bin, 'pip')) else ""

    def install(self):
        template = env.get_template('debianize.sh')
        output = template.render(
            follow_dependencies=self.options.get(
                'follow_dependencies', '.*').split(),
            maintainer=self.options.get('maintainer', None),
            pip_path=self.pip_path,
            fpm_path=self.fpm_path
        )
        executable = join(self.bin, 'debianize')
        with open(executable, 'w') as fh:
            fh.write(output)

        chmod(executable,
           stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH | \
            stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | \
            stat.S_IWUSR
        )

        return executable

    def update(self):
        pass
