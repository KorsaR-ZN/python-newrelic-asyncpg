#!/usr/bin/env python
import pathlib
from setuptools import setup, find_packages

__ROOT = pathlib.Path(__file__).parent

__version__ = '0.1.3'
__author__ = 'Stanislav Kiryukhin'
__license__ = "MIT"

with open(str(__ROOT / 'README.md')) as f:
    __description_long__ = f.read()

setup(
    name='newrelic-asyncpg',
    version=__version__,
    description='Unofficial asyncpg extensions for the NewRelic Python Agent',
    long_description=__description_long__,
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
