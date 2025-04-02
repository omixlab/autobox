from setuptools import setup, find_packages

setup(
    name='autobox',
    version='0.0.1',
    description='autobox: a cli tool to generate docking box configuration from PDB files',
    author='Frederico Schmitt Kremer',
    author_email='fred.s.kremer@gmail.com',
    requires=['biopython', 'pandas'],
    install_requires=['biopython', 'pandas'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'autobox = autobox.cli:main'
        ]
    }
)