#!/usr/bin/env python

from setuptools import setup,find_packages

setup(name='detrend_example',
      version='0.1.0',
      description='a detrend example',
      author='Zhangbei',
      author_email='rular099@gmail.com',
      packages=find_packages(),
      install_requires=['os','numpy','matplotlib','pandas','scipy'],
     )
