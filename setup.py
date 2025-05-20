from setuptools import setup

setup(
    name="pycount",
    version="1.0.0",
    package_dir={'': 'src'},
    packages=[''],
    entry_points={
        "console_scripts": [
            "pycount = cli:main"
        ],
    },
)