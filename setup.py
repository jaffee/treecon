from setuptools import setup

setup(
    name='treecon',
    version='0.0.0',
    author='Matthew Jaffee',
    description="Interface for display and navigation of tree-like data",
    packages=['treecon'],
    package_dir={'treecon': 'treecon'},
    install_requires=[
        'Flask'
    ],
    entry_points = {
        'console_scripts': [
            'treecon = treecon.__main__'
        ]
    }
)
