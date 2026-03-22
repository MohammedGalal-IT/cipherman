from setuptools import setup

setup(
    name='cipherman',
    version='1.0',
    description="A very basic CLI encryption tool for classical ecryption techniques",
    scripts=['bin/cipherman'],
    packages=['cipherman'],
#    install_requires=['cryptography'],
)
