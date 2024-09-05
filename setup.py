'Script to define package setup and installation'

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sdplus",
    version="0.1.0",
    author="Joshua Hurd",
    author_email="isorikk@gmail.com",
    description="A Python library for the ManageEngine ServiceDesk Plus API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/himea-saito/ManageEngine-SD-API",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests"
    ],
    python_requires='>=3.12'
)
