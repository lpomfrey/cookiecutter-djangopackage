# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from distutils import version


__version__ = '{{ cookiecutter.version }}'
version_info = version.StrictVersion(__version__).version
