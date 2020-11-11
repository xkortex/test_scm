from setuptools import find_packages, setup

packages = find_packages()
setup(
    name='test_scm',
    use_scm_version=True,
    script_name='setup.py',
    python_requires='>=3.6',
    packages=packages,
    setup_requires=['setuptools_scm'],
)
