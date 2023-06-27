#!/usr/bin/env python

import re
import os
import sys
from setuptools import find_packages, setup


name = 'wagtailmodelchooser'
package = 'wagtailmodelchooser'
description = 'Wagtail chooser panel generator for generic Django models'
url = 'https://github.com/Naeka/wagtailmodelchooser'
author = 'Naeka'
author_email = 'leo@naeka.fr'
license = 'BSD'


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)

version = get_version(package)

install_requires = [
    'Django>=3.2',
    'wagtail>=4.1',
]

# Testing dependencies
testing_extras = [
    # Required for running the tests
    'pytest-django>=3.2,<3.5',
    'pytest>=3.6',
    'pytest-cov>=2.5',
    'flake8>=2.4.0',

    # For PyPI installs
    'wheel==0.24.0',
]

# Documentation dependencies
documentation_extras = [
    'mkdocs==0.11.1',
]


setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras
    },
)
