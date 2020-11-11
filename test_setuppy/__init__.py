"""Docstring cause flit says I have to have one """

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
