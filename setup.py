from setuptools import find_packages, setup


__version__ = '1.0'

setup(name='couch_wrapper',
      version=__version__,
      author='Sigalei',
      author_email='contato@sigalei.com.br',
      url='https://github.com/sigalei/couchdb_wrapper',
      description='Wrapper to handle documents in couchdb.',
      packages=find_packages(),
      install_requires=[
          'cloudant>=2.12.0', 'pytz', 'pytest>=4.5.0'
      ],
      zip_safe=False)