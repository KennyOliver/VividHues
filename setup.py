from setuptools import setup

print("\033[93m" + "Installing VividHues..." + "\033[0m")

setup(
    name='VividHues', #needed to silence warnings (and to be a worthwhile package)
    url='https://github.com/KennyOliver/VividHues',
    author='Kenneth Oliver',
    author_email='kenny_oliver@icloud.com',
    packages=['VividHues'], #needed to actually package something
    # install_requires=['numpy'], #needed for dependencies
    version='2.7.3',
    license='AGPL', #license can be anything you like
    description='VividHues is a lightweight Python package for coloured strings in the Python console!',
    # long_description=open('README.txt').read(), #you need a readme eventually (there will be a warning)
)

print("\033[32m" + "\033[1m" + "Success!!! Have colourful fun! ;D" + "\033[0m")
