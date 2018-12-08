from setuptools import setup

setup(
    name='shoppinglist',
    version='0.1-dev',
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
