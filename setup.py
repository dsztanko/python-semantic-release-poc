import sys
from setuptools import setup

setup(
    name="python-semantic-release-poc",
    version="",
    packages=["sample"],
    url="https://github.com/dsztanko/python-semantic-release-poc",
    license="MIT",
)

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass