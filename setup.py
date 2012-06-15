#!/usr/bin/env python

from setuptools import setup, find_packages

import paypal

setup(
    name='django-paypal',
    version=".".join(map(str, paypal.__version__)),
    author='John Boxall',
    author_email='john@handimobility.ca',
    maintainer="Alejandro Gomez",
    maintainer_email="agoma8@gmail.com",
    url='http://github.com/agoma8/django-paypal',
    install_requires=[
        'Django>=1.0'
    ],
    description = 'A pluggable Django application for integrating PayPal Payments Standard or Payments Pro',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
