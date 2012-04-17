"""
Turn python packages into debian packages, including dependencies.

Blaat
"""
from setuptools import setup
from setuptools import find_packages

version = '0.1'

setup(name='avira.recipe.debianize',
      version=version,
      description="debianize",
      long_description=__doc__,
      classifiers=[],
      # Get strings from
      #http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Lars van de Kerkhof',
      author_email='lars@permanentmarkers.nl',
      url='https://github.com/specialunderwear/pm.recipe.debianize',
      license='CopyRight PermanentMarkers 2012',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['pm', 'recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'distribute',
        'Jinja2',
        # -*- Extra requirements: -*-
      ],
      entry_points={'zc.buildout': [
          'default = avira.recipe.debianize:Debianize']},
      )
