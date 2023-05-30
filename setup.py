from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='bitrixutils',
    version='0.1.0',
    description='Utilities for working with Bitrix CMS',
    long_description=readme,
    packages=find_packages(exclude=('tests',))
)
