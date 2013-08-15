#!python3.3
# -*- coding: utf-8 -*-
#from distutils.core import setup

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys
import os

DISTUTILS_DEBUG = True

py_version = sys.version_info[:2]
PY3 = py_version[0] == 3

if not PY3:
    raise RuntimeError('Python 3.x is required')

thisdir = os.path.dirname(__file__)

with open(os.path.join(thisdir, 'README.md')) as file:
    long_description = file.read()

setup(name = 'pyHexa',
      version = '0.0.2',  # major.minor.revision
      
      platforms = ['Linux', 'Windows'],
      url = 'https://github.com/Rod-Persky/pyHexa',
      
      classifiers = [
        'Development Status :: 3 - Alpha',
        
        'Topic :: Scientific/Engineering',
        
        'License :: OSI Approved :: Academic Free License (AFL)',
        
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        
        'Environment :: No Input/Output (Daemon)',  # No IO required
        
        'Natural Language :: English',
        
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: OS Independent',
        ],

      description = 'Python Hexapod WEB UI',
      long_description = long_description,
      license = 'Academic Free License ("AFL") v. 3.0',

      author = 'Rodney Persky',
      author_email = 'rodney.persky@gmail.com',

      packages = ['pyHexa'],
      package_dir = {'pyHexa': 'pyHexa'},
      
      zip_safe = True,
      include_package_data = True,
      
      py_modules = ['ez_setup'],
      
      install_requires=['bottle>=0.11.5',
                        'cherrypy>=3.2.4'],
      )
