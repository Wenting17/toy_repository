from pathlib import Path
from importlib import import_module
from setuptools import setup, find_packages


def read_file(file):
    file = Path(__file__).parent.absolute().joinpath(file)
    with file.open("r") as f:
        return f.read()


module_name = "toy_repository"
version = import_module("toy_repository").__version__


setup(
    name=module_name,
    version=version,
    description="create a new repository.",
    packages=find_packages(exclude=[]),
    author="Wenting Zhang",
    license="Apache License v2",
    package_data={"": ["*.*"]},
    url="",
    install_requires=read_file("requirements.txt").strip(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)