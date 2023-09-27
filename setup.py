import os
import re
import pathlib
from setuptools import setup, find_packages

regex = "^v(\d+\.\d+\.\d+)$"
TAG = os.getenv("TAG", "v0.0.0")
if not TAG or not re.search(regex, TAG):
    raise ValueError("TAG environment variable must be in the format v1.2.3")
version = re.search(regex, TAG).group(1)

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# The list of requirements
requirements = (HERE / "requirements.txt").read_text().split("\n")

setup(
    name="cornojob-killer",
    version=version,
    description="No more cornojobs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abstra-app/cornojob-killer",
    license="MIT",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "cornojob=cornojob_killer.cli:main",
        ],
    },
)
