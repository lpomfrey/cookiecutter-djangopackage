#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(package):
    '''
    Return package version as listed in `__version__` in `init.py`.
    '''
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]', init_py, re.MULTILINE
    ).group(1)


version = get_version('{{ cookiecutter.app_name }}')


requirements = [
    re.sub(r'\s*#.*$', '', x).strip() for x in
    open('requirements.txt').read().split('\n')
    if re.sub(r'\s*#.*$', '', x).strip()
]


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    args = {'version': version}
    print 'You probably want to also tag the version now:'
    print ' git tag -a release/{version} -m \'version {version}\''.format(
        **args)
    print ' git push --tags'
    sys.exit()


readme = open('README.rst').read()


setup(
    name='{{ cookiecutter.project_name }}',
    version=version,
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    include_package_data=True,
    install_requires=requirements,
    test_suite='runtests.runtests',
    tests_require=[],
    license='BSD',
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
