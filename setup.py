from setuptools import setup, find_packages

setup(
    name='viperlib',
    author='vipervit',
    licence='Apache',
    description='General use library.',
    version='0.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test*"])
)
