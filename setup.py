#!/usr/bin/env python

from setuptools import setup,find_packages

setup(name='detrend-example',
      version='0.1.0',
      description='a detrend example',
      author='Zhangbei',
      author_email='rular099@gmail.com',
      packages=find_packages(where='.'),
      py_modules=['detrend_example','main']
      install_requires=['numpy','matplotlib','pandas','scipy'],
     )
