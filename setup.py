from setuptools import find_packages, setup

packages = find_packages()
setup(
    name='test_scm',
    use_scm_version={
        'write_to': 'test_scm/_version.py',
        'write_to_template': '__version__ = "{version}"',
    },
    script_name='setup.py',
    python_requires='>=3.5',
    packages=packages,
    setup_requires=['setuptools_scm'],
)
