from setuptools import setup, find_packages

setup(
    name='viperlib',
    author='vipervit',
    author_email='vitolg1@gmail.com',
    license='Apache',
    description='General use library.',
    version='0.41',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test*"])
)
