import os
from setuptools import find_packages, setup
import versioneer

commands = versioneer.get_cmdclass().copy()
version = os.environ.get('TEST_SETUPPY_VERSION', versioneer.get_version())

packages = find_packages()
setup(
    name='test_setuppy',
    version=version,
    script_name='setup.py',
    python_requires='>=3.6',
    packages=packages,
    cmdclass=commands,
)
