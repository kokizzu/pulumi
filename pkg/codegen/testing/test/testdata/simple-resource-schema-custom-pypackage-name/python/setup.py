# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "0.0.0"
def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "example Pulumi Package - Development Version"


setup(name='custom_py_package',
      python_requires='>=3.7',
      version=VERSION,
      long_description=readme(),
      long_description_content_type='text/markdown',
      packages=find_packages(),
      package_data={
          'custom_py_package': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'importlib-metadata>=6.0.0,<7.0.0; python_version < "3.8"',
          'parver>=0.2.1',
          'pulumi',
          'semver>=2.8.1'
      ],
      zip_safe=False)
