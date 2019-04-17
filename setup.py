from setuptools import setup

version = None
with open('VERSION.txt', 'r') as fp:
    version = fp.read()

setup(
    name='shoppinglist',
    version=version,
    packages=['shoppinglist'],
    entry_points={
      'console_scripts': [
          'shoppinglist_launcher=shoppinglist.__main__:main'
      ]
    },
    url='',
    license='',
    author='Célian Garcia',
    author_email='celian.garcia1@gmail.com',
    description=''
)
