from setuptools import setup

setup(
    name='VividHues', #needed to silence warnings (and to be a worthwhile package)
    url='https://github.com/KennyOliver/VividHues',
    author='Kenneth Oliver',
    author_email='kenny_oliver@icloud.com',
    packages=['VividHues'], #needed to actually package something
    # install_requires=['numpy'], #needed for dependencies
    version='2.6.8',
    license='AGPL', #license can be anything you like
    description='VividHues is a lightweight Python package for coloured strings in the Python console!',
    # long_description=open('README.txt').read(), #you need a readme eventually (there will be a warning)
)
