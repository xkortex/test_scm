import os
from setuptools import find_packages, setup

setup(
    name='test_scm_sub',
    use_scm_version={
        'write_to': 'sub/_version.py',
        'write_to_template': '__version__ = "{version}"',
        'root': '..',
        'relative_to': __file__,
    },
    script_name='setup.py',
    python_requires='>=3.5',
    setup_requires=['setuptools_scm'],
    install_requires=['test-scm'],
    zip_safe=False,
)
