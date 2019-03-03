#!/usr/bin/env python
import pathlib
from setuptools import setup, find_packages

__ROOT = pathlib.Path(__file__).parent

__version__ = '0.1.4'
__author__ = 'Stanislav Kiryukhin'
__license__ = "MIT"

with open(str(__ROOT / 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='newrelic-asyncpg',
    version=__version__,
    description='Unofficial extension for the NewRelic Python Agent for support asyncpg database adapter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KorsaR-ZN/python-newrelic-asyncpg',
    author=__author__,
    author_email='korsar.zn@gmail.com',
    license=__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['asyncpg', 'newrelic', 'extensions'],
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    python_requires='>=3.5',
    install_requires=[
        'newrelic>=4.10.0.112',
    ],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
