import codecs
import io
import re
import sys

from setuptools import find_packages, setup

with io.open("dashuta/version.py", "rt", encoding="utf-8") as f:
    version = re.search(r'__version__ = [\'"]([^\'"]+)', f.read()).group(1)

with codecs.open("README.md", "r", "utf-8") as f:
    import re

    # cut the badges from the description and also the TOC which is currently not working on PyPi
    regex = r"([\s\S]*)## Quickstart"
    readme = f.read()

    long_description = re.sub(regex, "## Quickstart", readme, 1)
    assert long_description[:13] == "## Quickstart"  # Description should start with a headline (## Quickstart)

tests_require = ["pytest"]

extras_require = {"diagrams": ["pygraphviz"]}

extra_setuptools_args = {}
if "setuptools" in sys.modules:
    extras_require["test"] = ["pytest"]
    tests_require.append("pytest")

setup(
    name="dashuta",
    version=version,
    description="DASHUTA: - Unified Trading Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Igor Tarlinskiy",
    author_email="itarlinskiy@gmail.com",
    maintainer="Eldar Khayarov",
    maintainer_email="eldarhacks@gmail.com",
    url="http://github.com/atomicai/dashuta",
    packages=find_packages(exclude=["tests", "test_*"]),
    package_data={
        "transitions": ["py.typed", "data/*"],
        "transitions.tests": ["data/*"],
    },
    include_package_data=True,
    install_requires=["six"],
    extras_require=extras_require,
    tests_require=tests_require,
    license="MIT",
    download_url="https://github.com/atomicai/dashuta/archive/%s.tar.gz" % version,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    **extra_setuptools_args,
)
