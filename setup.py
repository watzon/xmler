from distutils.core import setup

version = '0.1.0'

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name = 'dict2xml',
    version = version,
    description = 'Converts a Python dictionary into a XML string with namespace support.',
    long_description = long_description,
    author = 'Chris Watson',
    author_email = 'chris@marginzero.co',
    license = 'LICENCE',
    url = 'https://github.com/iDev0urer/dict2xml',
    py_modules = ['dict2xml'],
    download_url = 'https://pypi.python.org/packages/source/d/dict2xml/dict2xml-%s.tar.gz?raw=true' % (version),
    platforms='Cross-platform',
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3'
    ],
)
