from setuptools import setup, find_packages
from randw.words import __title__, __version__, __author__, __license__

long_description = open('README.md').read()

setup(
    name=__title__,
    version=__version__,
    author=__author__,
    license=__license__,
    description="A random generator of English nouns and adjectives",
    url="https://github.com/evan-blaine/randw",
    author_email="evanblaineadams@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    platforms=["any"],
    package_data = {
        '':['data/*.txt']
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)