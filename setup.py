from setuptools import setup, find_packages

setup(
    name="datacleaner",
    version="0.1.0",
    description="A Python package for automating data cleaning tasks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Andy Yang",
    author_email="andyyang1188@gmail.com",
    url="https://github.com/andyy2000/datacleaner",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
