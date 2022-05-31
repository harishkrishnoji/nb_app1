from setuptools import find_packages, setup


setup(
    name='maintenance-notices',
    version='0.1',
    description='A Nautobot plugin for tracking maintenance notices',
    author='Harish Krishnoji',
    packages=find_packages(),
    include_package_data=True,
)
