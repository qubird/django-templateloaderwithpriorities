from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='django-templateloaderwithpriorities',
      version=version,
      description="A Django Template Loader with priorities",
      long_description=open("README.rst").read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
      keywords='django template loader',
      author='Vincenzo E. Antignano (@qubird)',
      author_email='@qubird',
      url='https://github.com/qubird/django-templateloaderwithpriorities',
      license='GNU General Public License (GPL)',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'django>=1.3',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
