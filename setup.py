import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="initproject",
    version="0.0.1",
    author="Xenia Sprottenfraulein",
    author_email="mslaimagulbe@example.com",
    description="Python project structure initialization tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sprottenfraulein/initproject",
    packages=setuptools.find_packages(),
)
