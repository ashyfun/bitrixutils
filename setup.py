from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

name = 'bitrixutils'
packages = [
    name + '.' + pkg
    for pkg in find_packages(where='src', exclude=('tests',))
]

setup(
    name=name,
    version='0.1.0',
    description='Utilities for working with Bitrix CMS',
    long_description=readme,
    packages=packages,
    package_dir={
        name: 'src',
    },
    entry_points={
        'console_scripts': ('{0} = {0}.cli:cli'.format(name),),
    }
)
