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
    license='AGPLv3 or later',
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
        'License :: OSI Approved '
        ':: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: System :: Networking :: Monitoring'
    ]
)
