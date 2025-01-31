# from distutils.core import setup
from setuptools import setup


long_description = '''
Iterable Python is a Python client that wraps the Iterable Api.
Originally developed by Carter Hickingbotham.  Current version is 1.2
'''

setup(
	name='iterablepythonwrapper',
	packages=['iterablepythonwrapper'],
	url='https://github.com/carter-j-h/iterable-python-wrapper',
	author='Carter Hickingbotham',
	author_email='carterhickingbotham@gmail.com',
	license= 'MIT',
	version='1.2',	
	install_requires=['peppercorn==0.6'],
	keywords = ['Iterable', 'API', 'Wrapper', 'Client', 'Python'],
    description='Python Client for the Iterable API',
    long_description=long_description

	)
