from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-multiline-links",
    description="Make multiple newline separated URLs clickable in Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-multiline-links",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-multiline-links/issues",
        "CI": "https://github.com/simonw/datasette-multiline-links/actions",
        "Changelog": "https://github.com/simonw/datasette-multiline-links/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_multiline_links"],
    entry_points={"datasette": ["multiline_links = datasette_multiline_links"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
