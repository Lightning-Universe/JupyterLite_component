#!/usr/bin/env python

import os
from typing import List

from setuptools import find_packages, setup


def _load_requirements(
    path_dir: str, file_name: str = "requirements.txt", comment_char: str = "#"
) -> List[str]:
    """Load requirements from a file.
    >>> _load_requirements(_PATH_ROOT)
    ['numpy...', 'torch..."]
    """
    with open(os.path.join(path_dir, file_name)) as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = []
    for ln in lines:
        # filer all comments
        if comment_char in ln:
            char_idx = min(ln.index(ch) for ch in comment_char)
            ln = ln[:char_idx].strip()
        # skip directly installed dependencies
        if (
            ln.startswith("http")
            or ln.startswith("git")
            or ln.startswith("-r")
            or "@" in ln
        ):
            continue
        if ln:  # if requirement is not empty
            reqs.append(ln)
    return reqs


_PATH_ROOT = os.path.realpath(os.path.dirname(__file__))
BASE_REQUIREMENTS = _load_requirements(
    path_dir=_PATH_ROOT, file_name="requirements.txt"
)

setup(
    name="lai_jupyterlite",
    version="0.0.1",
    description="Describe Your Cool Component",
    author="Aniket Maurya",
    author_email="aniket@lightning.ai",
    url="https://github.com/Lightning-AI/LAI-JupyterLite-Component",
    install_requires=BASE_REQUIREMENTS,
    packages=find_packages(),
)
