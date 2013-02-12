from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='sphinx-autodoc-source-generator',
      version=version,
      description="This script will traverse a tree of Python modules and create sphinx RST",
      long_description="""\
source (using the autodoc extension) that reflects the tree.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='sphinx autodoc',
      author='Robin Keller',
      author_email='rkeller@cars.com',
      url='https://github.com/cars-sm/sphinx-autodoc-source-generator',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      scripts=[
            "sphinx-autodoc-sourcegen.py"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
