from setuptools import setup

setup(
    name='cipherman',
    version='1.3.0',
    description="A very basic CLI encryption tool for classical encryption techniques",
    scripts=['bin/cipherman'],
    packages=['cipherman'],
    install_requires=['numpy', 'sympy', 'argcomplete'],
)
