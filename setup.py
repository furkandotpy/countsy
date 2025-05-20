from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="pycount",
    version="1.0.0",
    author="Furkan Tandogan",
    description="Count lines of Python code in directories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "pycount=cli:main"
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)