# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dealer/__init__.py
from dealer import __version__ as version

setup(
	name='dealer',
	version=version,
	description='Ventas de Carros',
	author='Josmel Diaz',
	author_email='josmeldiaz21@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
