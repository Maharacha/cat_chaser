# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Cat chaser',
    version='0.1.0',
    description='Code for the cat chaser.',
    long_description=readme,
    author='Joakim Nyman',
    author_email='joakim.nyman86@gmail.com',
    url='https://github.com/Maharacha/cat_chaser',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

