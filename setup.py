# define all the packages and required tools
from setuptools import setup

setup(
    name='simulator',
    packages=['simulator'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)