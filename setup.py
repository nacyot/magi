"""
Magi
====

Networked resource monitoring tool.

"""
from setuptools import setup


setup(
    name='Magi',
    version='dev',
    description='Networked resource monitoring tool',
    long_description=__doc__,
    url='https://github.com/smartstudy/magi',
    author='Jihyeok Seo',
    author_email='me@limeburst.net',
    maintainer='SMARTSTUDY D9',
    maintainer_email='d9@smartstudy.co.kr',
    license='MIT',
    zip_safe=False,
    packages=['magi', 'magi.web'],
    package_data={
        'magi.web': ['templates/*.*', 'static/*.*']
    },
    install_requires=[
        'Flask',
        'SQLAlchemy',
        'click'
    ],
    entry_points={
        'console_scripts': ['magi = magi.cli:cli']
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: System :: Networking :: Monitoring'
    ]
)
