#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='pw',
    version='1.0',
    description='Password storage and retrieval tool',
    author='David Rosson',
    author_email='david.rosson@gmail.com',
    packages=find_packages(),
    scripts=['pw-encryptor', 'pw'],
    install_requires=['pycrypto', 'pyperclip']
)

