from setuptools import setup

print("\033[93m" + "Installing VividHues..." + "\033[0m")

setup(
    name='VividHues',
    url='https://github.com/KennyOliver/VividHues',
    author='Kenneth Oliver',
    author_email='kenny_oliver@icloud.com',
    packages=['VividHues'],
    version='4.2.12',
    license='AGPL-v3',
    description='VividHues: super lite package for coloured strings in Python!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

print("\033[32m" + "\033[1m" + "VividHues was installed successfully! Have colorful fun! :D" + "\033[0m")
