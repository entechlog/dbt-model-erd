#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dbt-erd",
    version="1.0.0",
    author="Entechlog",
    description="Generate entity-relationship diagrams for dbt models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/entechlog/dbt-erd",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pyyaml>=5.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.5b0",
            "flake8>=3.9.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dbt-erd=dbt_erd:main",
        ],
    },
    include_package_data=True,
)
