from setuptools import setup

# Use a consistent encoding

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
# Read the contents of the README file

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django3-dpa-chile",
    version="0.4.0",
    description="Political-Administrative Division of Chile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zubus/django3-dpa-chile",
    author="Cristian Zúñiga",
    author_email="contacto@nyumba.cl",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Spanish",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="django chile regiones comunas provincias",
    packages=[
        "d3_dpa_chile",
        "d3_dpa_chile.migrations",
        "d3_dpa_chile.management",
        "d3_dpa_chile.management.commands",
    ],
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
        "requests",
    ],
)
