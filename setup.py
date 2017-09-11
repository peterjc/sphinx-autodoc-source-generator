from setuptools import setup, find_packages
import sys, os

version = '0.1.1'

setup(name='sphinx-autodoc-source-generator',
      version=version,
      description="This script will traverse a tree of Python modules and create sphinx RST",
      long_description="""Script to traverse a tree of Python modules and create
API documentation as reStructuredText (RST) markup using the module docstrings
via sphinx and the autodoc extension.""",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Intended Audience :: Developers',
          'Framework :: Sphinx',
          'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Documentation',
          'Topic :: Documentation :: Sphinx',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Documentation',
      ],
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
