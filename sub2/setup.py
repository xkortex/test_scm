import os
from setuptools import find_packages, setup

setup(
    name='test_scm_sub2',
    use_scm_version={
        'root': '..',
    },
    script_name='setup.py',
    python_requires='>=3.5',
    setup_requires=['setuptools_scm'],
)
