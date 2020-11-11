from setuptools import find_packages, setup

setup(
    name='test_scm.sub',
    use_scm_version={
        'write_to': 'test_scm/_version.py',
        'write_to_template': '__version__ = "{version}"',
        'root': '.',
        # 'relative_to': '__file__',
    },
    script_name='setup.py',
    python_requires='>=3.6',
    setup_requires=['setuptools_scm'],
)
