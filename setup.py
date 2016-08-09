from distutils.core import setup

version = '0.1.0'

setup(
    name = 'xmler',
    version = version,
    description = 'Converts a Python dictionary into a XML string with namespace support.',
    long_description = "Long description and usage instructions can be found at https://github.com/iDev0urer/xmler",
    author = 'Chris Watson',
    author_email = 'chris@marginzero.co',
    license = 'LICENCE',
    url = 'https://github.com/iDev0urer/xmler',
    py_modules = ['xmler'],
    download_url = 'https://pypi.python.org/packages/source/d/xmler/xmler-%s.tar.gz?raw=true' % (version),
    platforms='Cross-platform',
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3'
    ],
)
