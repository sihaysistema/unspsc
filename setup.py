# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in unspsc/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('unspsc/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='unspsc',
	version=version,
	description='UNSPSC son las iniciales de United Nations Standard Products and Services Code. Es un sistema de cifrado que clasifica productos y servicios para fines comerciales a escala mundial.',
	author='Si Hay Sistema',
	author_email='m.monroyc22@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
