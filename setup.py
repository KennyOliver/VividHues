from setuptools import setup

"""
Setup file for VividHues
"""

import codecs
import os.path


NAME = "VividHues"
print("\033[93m" + f"Installing {NAME}..." + "\033[0m")
setup(
    name="VividHues",
    url=f"https://github.com/KennyOliver/{NAME}",
    author="Kenneth Oliver",
    author_email="kenny_oliver@icloud.com",
    packages=[NAME],
    version="5.2.8",
    license="AGPL-3.0",
    description=f"{NAME}: super lite package for colored strings in Python!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Terminals",
    ]
)
print("\033[32m" + "\033[1m" + f"{NAME} was installed successfully! Have colorful fun! :D" + "\033[0m")
