from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='s3ninja',
      version=version,
      description="compress & upload files to s3 reliably",
      classifiers=[], 
      keywords='s3 upload compress',
      author='Padmakar Ojha',
      author_email='padmakarojha@gmail.com',
      url='https://pip.pypa.io/',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["click", "future", "boto"],
      entry_points={
          'console_scripts': [
              's3ninja = s3ninja.main:main',
          ]
      },
     )
