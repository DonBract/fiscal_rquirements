# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in fiscal_requirements/__init__.py
from fiscal_requirements import __version__ as version

setup(
	name='fiscal_requirements',
	version=version,
	description='modulo fiscal que tiene los elementos necesarios que exigen las leyes colombianas',
	author='donato',
	author_email='donato1357@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
