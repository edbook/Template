# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages

__version__ = 'unknown'
for line in open('sphinxcontrib/katex.py'):
    if line.startswith('__version__'):
        exec(line)
        break


def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")


requires = readfile("requirements.txt")

long_desc = """
    Sphinx extension using KaTeX to render instead of MathJax with custom functionality. Based largely 
    on (https://github.com/hagenw/sphinxcontrib-katex) and the build in mathjax extension for Sphinx
    """

setup(
    name='sphinxcontrib-katex',
    license='MIT',
    author='Arnór Pétur Marteinsson',
    long_description=long_desc,
    zip_safe=False,
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
