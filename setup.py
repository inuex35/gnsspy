"""
GNSSpy setup file
Mustafa Serkan ISIK and Volkan Ozbey
"""
from setuptools import setup, find_packages
import re
import os

def load_requirements(fname):
    """Load requirements from a requirements.txt file."""
    requirements = []
    if os.path.exists(fname):
        with open(fname, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    requirements.append(line)
    return requirements

def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)

setup(
  name = 'gnsspy',
  packages = find_packages(),
  install_requires=load_requirements("requirements.txt"),
  include_package_data = True,
  package_data = {"gnsspy.doc": ["IGSList.txt"],
                  "gnsspy.io" : ["CRX2RNX","crx2rnx.exe","RNX2CMP_LICENSE.txt"]},
  data_files = [("", ["LICENSE"])],
  version = get_property('__version__', 'gnsspy'),
  description = 'Python Toolkit for GNSS Data',
  author = get_property('__author__', 'gnsspy'),
  author_email = 'isikm@itu.edu.tr - ozbeyv@itu.edu.tr',
  license = 'MIT',
  url = 'https://github.com/GNSSpy-Project/gnsspy',
  download_url = 'https://github.com/GNSSpy-Project/gnsspy/archive/0.1.tar.gz',
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Scientific/Engineering',
  ],
  python_requires='>=3.6',
  zip_safe=False
)   

