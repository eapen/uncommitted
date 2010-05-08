# This setup.py was generated automatically by Pyron.
# For details, see http://pypi.python.org/pypi/pyron/

from setuptools import setup, find_packages

setup(
    name = 'uncommitted',
    version = '1.2',
    description = u'Scan Version Control For Uncommitted Changes',
    long_description = u'\nOriginally Created by Brandon Craig Rhodes\nThis is my forked version with Git support and defaulting to search by path rather than locate',
    author = 'George Eapen',
    author_email = 'github@eapen.in',
    url = 'http://github.com/eapen/uncommitted/',
    classifiers = ['Development Status :: 5 - Production/Stable', 'Environment :: Console', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Topic :: Software Development :: Version Control', 'Topic :: Utilities'],

    package_dir = {'': 'src'},
    packages = find_packages('src'),
    include_package_data = True,
    install_requires = [],
    entry_points = '[console_scripts]\uncommitted = uncommitted.command:main\n',
    )
