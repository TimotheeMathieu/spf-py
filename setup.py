from setuptools import setup, find_packages

setup(
    name='spf_py',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'mistletoe',
    ],
    entry_points={
        'console_scripts': [
            'spf = spf_py.cli:cli',
        ],
    },
)
