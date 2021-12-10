from setuptools import setup

"""
Setup file for VividHues
"""

import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


NAME = "VividHues"
print("\033[93m" + f"Installing {NAME}..." + "\033[0m")
setup(
    name="VividHues",
    url=f"https://github.com/KennyOliver/{NAME}",
    author="Kenneth Oliver",
    author_email="kenny_oliver@icloud.com",
    packages=[NAME],
    version=get_version(f"{NAME}/__init__.py"),
    license="AGPL-3.0",
    description=f"{NAME}: super lite package for colored strings in Python!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
print("\033[32m" + "\033[1m" + f"{NAME} was installed successfully! Have colorful fun! :D" + "\033[0m")
