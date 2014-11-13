from setuptools import setup, find_packages

from magi.version import VERSION


def readme():
    with open('README.rst') as f:
        return f.read()


install_requires = [
    'Flask',
    'SQLAlchemy'
]


setup(
    name='Magi',
    version=VERSION,
    description='Networked resource monitoring tool',
    long_description=readme(),
    url='https://github.com/limeburst/magi',
    author='Jihyeok Seo',
    author_email='me@limeburst.net',
    license='AGPLv3 or later',
    packages=find_packages(),
    install_requires=install_requires,
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
